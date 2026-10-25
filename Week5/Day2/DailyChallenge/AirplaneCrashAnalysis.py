"""Week 5 Day 2 Daily Challenge: Airplane Crashes and Fatalities through 2023.
Run: py AirplaneCrashAnalysis.py
Requires: pandas numpy scipy matplotlib seaborn
"""
from pathlib import Path
from urllib.request import urlopen
import io
import re
import zipfile
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results'
OUT.mkdir(exist_ok=True)
URL = ('https://github.com/devtlv/Datasets-DA-Bootcamp-2-/raw/refs/heads/main/'
       'W4%20Gen%20AI/W4D3/Airplane%20Crashes%20and%20Fatalities%20upto%202023.zip')
sns.set_theme(style='whitegrid')


def read_data():
    local = list(ROOT.glob('*.zip'))
    if local:
        print('Loading local ZIP:', local[0].name)
        payload = local[0].read_bytes()
    else:
        print('Downloading source ZIP...')
        try:
            with urlopen(URL, timeout=45) as response:
                payload = response.read()
        except Exception as exc:
            raise RuntimeError('Download failed. Save the assignment ZIP beside this script and rerun.') from exc
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        csvs = [n for n in archive.namelist() if n.lower().endswith('.csv') and not Path(n).name.startswith('._')]
        if not csvs:
            raise ValueError('ZIP contains no CSV files')
        with archive.open(csvs[0]) as stream:
            try:
                return pd.read_csv(stream, encoding='utf-8', low_memory=False)
            except UnicodeDecodeError:
                stream.seek(0)
                return pd.read_csv(stream, encoding='latin-1', low_memory=False)


def find_column(frame, *aliases):
    normalized = {re.sub(r'[^a-z0-9]', '', str(c).lower()): c for c in frame.columns}
    for name in aliases:
        key = re.sub(r'[^a-z0-9]', '', name.lower())
        if key in normalized:
            return normalized[key]
    return None


def save_chart(filename):
    plt.tight_layout()
    plt.savefig(OUT / filename, dpi=160, bbox_inches='tight')
    plt.close()


raw = read_data()
print('Original dataset:', raw.shape)
print('Columns:', list(raw.columns))
print('Missing values before cleaning:\n', raw.isna().sum().to_string())

# Standardize known variations in column names without assuming an exact schema.
date_col = find_column(raw, 'Date', 'Crash Date', 'Crash_Date')
fatal_col = find_column(raw, 'Fatalities', 'Fatalities Aboard', 'Deaths')
aboard_col = find_column(raw, 'Aboard', 'Total Aboard', 'Passengers Aboard')
ground_col = find_column(raw, 'Ground', 'Ground Fatalities', 'Ground Deaths')
location_col = find_column(raw, 'Location', 'Crash Location')
operator_col = find_column(raw, 'Operator', 'Airline')
if date_col is None or fatal_col is None:
    raise ValueError('Expected date and fatalities columns. Available: ' + ', '.join(map(str, raw.columns)))

frame = pd.DataFrame(index=raw.index)
frame['date'] = pd.to_datetime(raw[date_col], errors='coerce')
# Some sources use mixed date formats; retry unresolved dates with day-first parsing.
if frame['date'].isna().any():
    unresolved = frame['date'].isna()
    frame.loc[unresolved, 'date'] = pd.to_datetime(raw.loc[unresolved, date_col], errors='coerce', dayfirst=True)
frame['fatalities'] = pd.to_numeric(raw[fatal_col], errors='coerce')
frame['aboard'] = pd.to_numeric(raw[aboard_col], errors='coerce') if aboard_col else np.nan
frame['ground_fatalities'] = pd.to_numeric(raw[ground_col], errors='coerce') if ground_col else np.nan
frame['location'] = raw[location_col].astype('string').str.strip() if location_col else pd.Series('Unknown', index=raw.index, dtype='string')
frame['operator'] = raw[operator_col].astype('string').str.strip() if operator_col else pd.Series('Unknown', index=raw.index, dtype='string')
frame['location'] = frame['location'].fillna('Unknown').replace('', 'Unknown')
frame['operator'] = frame['operator'].fillna('Unknown').replace('', 'Unknown')

# Remove exact duplicate source rows, rather than distinct incidents with matching counts.
frame = frame.loc[~raw.duplicated()].copy()
frame = frame.dropna(subset=['date'])
frame = frame[(frame['date'].dt.year <= 2023) & (frame['date'].dt.year >= 1900)]
frame.loc[frame['fatalities'] < 0, 'fatalities'] = np.nan
frame.loc[frame['aboard'] < 0, 'aboard'] = np.nan
frame.loc[frame['ground_fatalities'] < 0, 'ground_fatalities'] = np.nan
# Fatalities typically means deaths among people aboard, not ground deaths.
invalid = frame['aboard'].notna() & frame['fatalities'].notna() & (frame['fatalities'] > frame['aboard'])
frame.loc[invalid, 'fatalities'] = np.nan
frame['year'] = frame['date'].dt.year
frame['decade'] = (frame['year'] // 10) * 10
frame['survivors'] = np.where(frame['aboard'].gt(0) & frame['fatalities'].notna(), frame['aboard'] - frame['fatalities'], np.nan)
frame['survival_rate'] = np.where(frame['aboard'].gt(0) & frame['fatalities'].notna(), frame['survivors'] / frame['aboard'], np.nan)
frame['fatality_rate'] = 1 - frame['survival_rate']
frame.to_csv(OUT / 'cleaned_crashes.csv', index=False)

# Annual incident counts and recorded onboard fatalities (not a per-flight risk rate).
annual = frame.groupby('year').agg(crashes=('year', 'size'), recorded_fatalities=('fatalities', 'sum')).reset_index()
annual.to_csv(OUT / 'annual_trends.csv', index=False)
decades = frame.groupby('decade').agg(crashes=('year', 'size'), mean_fatalities=('fatalities', 'mean'), median_fatalities=('fatalities', 'median'), mean_survival_rate=('survival_rate', 'mean')).reset_index()
decades.to_csv(OUT / 'decade_statistics.csv', index=False)
locations = frame['location'].value_counts().head(12)
locations.rename_axis('location').reset_index(name='crashes').to_csv(OUT / 'top_locations.csv', index=False)

# SciPy: descriptive statistics and Welch's t-test comparing the last two decades
# with at least 10 valid fatality observations each.
valid_fatalities = frame['fatalities'].dropna()
valid_survival = frame['survival_rate'].dropna()
eligible = [(int(dec), group['fatalities'].dropna().to_numpy()) for dec, group in frame.groupby('decade') if group['fatalities'].notna().sum() >= 10]
test_text = 'Insufficient decade samples for a meaningful Welch t-test.'
if len(eligible) >= 2:
    (dec1, a), (dec2, b) = eligible[-2:]
    test = stats.ttest_ind(a, b, equal_var=False)
    test_text = (f'Welch t-test: {dec1}s vs {dec2}s; n={len(a)} vs {len(b)}; '
                 f'means={a.mean():.2f} vs {b.mean():.2f}; '
                 f't={test.statistic:.4f}; p={test.pvalue:.6g}. '
                 + ('Evidence of different mean fatalities per recorded crash (p < 0.05).'
                    if test.pvalue < 0.05 else 'Insufficient evidence of different mean fatalities per recorded crash (p >= 0.05).'))

# Plot 1: time series
plt.figure(figsize=(11, 5))
sns.lineplot(data=annual, x='year', y='crashes')
plt.title('Recorded airplane crashes by year')
plt.xlabel('Year'); plt.ylabel('Number of recorded crashes')
save_chart('01_crashes_by_year.png')

# Plot 2: onboard fatalities per year
plt.figure(figsize=(11, 5))
sns.lineplot(data=annual, x='year', y='recorded_fatalities')
plt.title('Recorded onboard fatalities by year')
plt.xlabel('Year'); plt.ylabel('Onboard fatalities (known records)')
save_chart('02_fatalities_by_year.png')

# Plot 3: top named locations (NOT regions unless the source has region data)
plt.figure(figsize=(11, 6))
sns.barplot(x=locations.values, y=locations.index.astype(str), color='steelblue')
plt.title('Most frequently listed crash locations')
plt.xlabel('Number of recorded crashes'); plt.ylabel('Location as recorded')
save_chart('03_top_locations.png')

# Plot 4: fatalities distribution
if not valid_fatalities.empty:
    plt.figure(figsize=(10, 5))
    sns.histplot(valid_fatalities, bins=35)
    plt.title('Distribution of fatalities per recorded crash')
    plt.xlabel('Onboard fatalities'); plt.ylabel('Number of crashes')
    save_chart('04_fatalities_histogram.png')

# Plot 5: survival rates (only incidents with valid aboard and fatalities counts)
if not valid_survival.empty:
    plt.figure(figsize=(10, 5))
    sns.histplot(valid_survival, bins=20)
    plt.title('Distribution of estimated onboard survival rates')
    plt.xlabel('Survival rate (0–1)'); plt.ylabel('Number of crashes')
    save_chart('05_survival_rates.png')

# Plot 6: comparison across decades
plt.figure(figsize=(11, 5))
sns.barplot(data=decades, x='decade', y='mean_fatalities', color='steelblue')
plt.title('Mean onboard fatalities per recorded crash by decade')
plt.xlabel('Decade'); plt.ylabel('Mean onboard fatalities')
plt.xticks(rotation=45)
save_chart('06_mean_fatalities_by_decade.png')

# Generate a written report from the actual dataset rather than invented figures.
mean_f = valid_fatalities.mean() if len(valid_fatalities) else float('nan')
median_f = valid_fatalities.median() if len(valid_fatalities) else float('nan')
std_f = valid_fatalities.std(ddof=1) if len(valid_fatalities) > 1 else float('nan')
mean_s = valid_survival.mean() if len(valid_survival) else float('nan')
median_s = valid_survival.median() if len(valid_survival) else float('nan')
std_s = valid_survival.std(ddof=1) if len(valid_survival) > 1 else float('nan')
peak = annual.loc[annual['crashes'].idxmax()] if len(annual) else None
report = f'''# Week 5 Day 2 — Daily Challenge: Airplane Crash Analysis

## 1. Data and cleaning
Source: {URL}
Original records: {len(raw):,}; retained dated records through 2023: {len(frame):,}.
Records with known onboard fatalities: {len(valid_fatalities):,}.
Records with calculable onboard survival rates: {len(valid_survival):,}.
Converted dates and numeric columns, removed exact duplicates, handled missing data,
and excluded impossible onboard fatality counts greater than aboard counts.
Unknown fatalities or passenger counts remain missing rather than being assumed zero.

## 2. Exploratory data analysis
Recorded crashes: {len(frame):,}.
Sum of known onboard fatalities: {valid_fatalities.sum():,.0f}.
Mean fatalities per crash with known fatalities: {mean_f:.2f}.
Median fatalities per crash with known fatalities: {median_f:.2f}.
Standard deviation of fatalities (sample): {std_f:.2f}.
Mean of incident-level survival rates: {mean_s:.2%}.
Median incident-level survival rate: {median_s:.2%}.
Standard deviation of incident-level survival rates: {std_s:.4f}.
Year with most recorded crashes: {int(peak['year']) if peak is not None else 'N/A'} ({int(peak['crashes']) if peak is not None else 0}).

## 3. Statistical hypothesis test
Null hypothesis: mean onboard fatalities per recorded crash are equal in the two compared decades.
Alternative hypothesis: these means differ.
{test_text}
This is an observational comparison, not evidence that the decade caused differences.
The test assumes independent observations; skewed fatality counts and uneven coverage
can affect its reliability.

## 4. Visualizations
- 01_crashes_by_year.png — time series of recorded crashes.
- 02_fatalities_by_year.png — known onboard fatalities over time.
- 03_top_locations.png — most common named locations (not aggregated geographic regions).
- 04_fatalities_histogram.png — fatalities distribution.
- 05_survival_rates.png — incident-level survival-rate distribution.
- 06_mean_fatalities_by_decade.png — mean fatalities by decade.

## 5. Insights and limitations
The peak year is {int(peak['year']) if peak is not None else 'unknown'} in this recorded dataset.
The mean and median of fatalities should be compared because rare large incidents
can pull the mean upward. Survival rates are calculated only where both aboard
and onboard fatality counts are valid. Mean incident survival rate gives each
incident equal weight; it is not the survival rate of all people aboard combined.

These data contain crash records, not total flights or passenger miles.
Therefore a decrease in crash counts does NOT by itself prove flying became safer:
flight volumes, reporting coverage, aviation technology, and historical data
completeness can all change. This is a descriptive study, not a causal analysis.

## 6. Tools used
Pandas: import, cleaning, grouping, aggregation, and CSV export.
NumPy: conditional survival calculations and numerical arrays.
SciPy: descriptive statistical comparisons and Welch's independent-samples t-test.
Matplotlib and Seaborn: six charts exported to PNG.
'''
(OUT / 'analysis_report.md').write_text(report, encoding='utf-8')
print('\n' + report)
print('Saved charts, report, and CSV tables in:', OUT)
