"""Week 5 Day 4 - Exercises XP: Data Visualization (all six exercises)."""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import quote
import io
import zipfile

import matplotlib
matplotlib.use('Agg')  # Save plots even without a GUI display.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

BASE = Path(__file__).resolve().parent
RESULTS = BASE / 'results'
RESULTS.mkdir(exist_ok=True)
sns.set_theme(style='whitegrid')

print('EXERCISE 1: Understanding Data Visualization')
print('Data visualization makes patterns, trends, outliers, and comparisons easier to understand and communicate.')
print('A line graph shows how a numerical quantity changes across ordered points, especially over time.\n')

print('EXERCISE 2: Weekly temperatures')
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [72, 74, 76, 80, 82, 78, 75]
fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(days, temperatures, marker='o')
ax.set(xlabel='Day', ylabel='Temperature (°F)', title='Temperature Variation Over a Week')
fig.tight_layout()
fig.savefig(RESULTS / 'exercise2_temperature_line.png', dpi=160)
plt.close(fig)

print('EXERCISE 3: Monthly sales')
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [5000, 5500, 6200, 7000, 7500]
fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(months, sales, color='steelblue')
ax.set(xlabel='Month', ylabel='Sales Amount ($)', title='Monthly Retail Sales')
fig.tight_layout()
fig.savefig(RESULTS / 'exercise3_monthly_sales_bar.png', dpi=160)
plt.close(fig)

URL = ('https://github.com/devtlv/Datasets-GEN-AI-Bootcamp/raw/refs/heads/main/'
       'Week%203/W3D1%20-%20Data%20Visualization/Student%20Mental%20health.zip')

def load_data():
    local = BASE / 'Student Mental health.zip'
    if local.exists():
        data = local.read_bytes()
        print('Using locally downloaded ZIP.')
    else:
        print('Downloading Student Mental health ZIP...')
        try:
            with urlopen(URL, timeout=45) as response:
                data = response.read()
        except Exception as exc:
            raise RuntimeError('Could not download the dataset. Save the ZIP from the assignment link beside ExercisesXP.py as "Student Mental health.zip" and rerun.') from exc
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        candidates = [n for n in archive.namelist() if not n.startswith('__MACOSX/') and not Path(n).name.startswith('._') and n.lower().endswith(('.csv', '.xlsx', '.xls'))]
        if not candidates:
            raise ValueError('The ZIP contains no CSV or Excel dataset.')
        name = sorted(candidates)[0]
        print('Reading:', name)
        with archive.open(name) as f:
            contents = f.read()
        if name.lower().endswith('.csv'):
            try:
                return pd.read_csv(io.BytesIO(contents))
            except UnicodeDecodeError:
                return pd.read_csv(io.BytesIO(contents), encoding='latin-1')
        return pd.read_excel(io.BytesIO(contents))

df = load_data()
df.columns = df.columns.astype(str).str.strip()
print('Dataset shape:', df.shape)
print('Columns:', df.columns.tolist())

# Match column names flexibly in case of minor whitespace/case differences.
def col(name):
    mapping = {''.join(c.lower().split()): c for c in df.columns}
    key = ''.join(name.lower().split())
    if key not in mapping:
        raise KeyError(f'Required column {name!r} not found. Available columns: {df.columns.tolist()}')
    return mapping[key]

cgpa_col = col('What is your CGPA?') if any('cgpa' in c.lower() for c in df.columns) else col('CGPA')
gender_col = col('Choose your gender')
anxiety_col = col('Do you have Anxiety?')
age_col = col('Age')
panic_col = col('Do you have Panic attack?')

print('\nEXERCISE 4: CGPA distribution')
cgpa = df[cgpa_col].astype('string').str.strip().replace({'<NA>': pd.NA})
# Values in this dataset are usually ranges, such as '3.00 - 3.49'.
order = sorted(cgpa.dropna().unique(), key=lambda s: float(__import__('re').search(r'\d+(?:\.\d+)?', str(s)).group()) if __import__('re').search(r'\d+(?:\.\d+)?', str(s)) else float('inf'))
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(x=cgpa.dropna().astype(str), discrete=True, color='teal', ax=ax)
# histplot on categorical data displays counts for each CGPA range.
ax.set(xlabel='CGPA Category', ylabel='Number of Students', title='Distribution of Student CGPA Categories')
ax.tick_params(axis='x', rotation=35)
fig.tight_layout()
fig.savefig(RESULTS / 'exercise4_cgpa_histogram.png', dpi=160)
plt.close(fig)
print(cgpa.value_counts(dropna=False).to_string())

print('\nEXERCISE 5: Anxiety proportions by gender')
subset = df[[gender_col, anxiety_col]].dropna().copy()
subset['anxiety_numeric'] = subset[anxiety_col].astype(str).str.strip().str.lower().map({'yes': 1, 'no': 0})
subset[gender_col] = subset[gender_col].astype(str).str.strip()
subset = subset.dropna(subset=['anxiety_numeric'])
if subset.empty:
    raise ValueError('No valid Yes/No anxiety responses were found.')
anxiety_summary = subset.groupby(gender_col)['anxiety_numeric'].agg(['mean', 'count']).rename(columns={'mean': 'proportion_anxiety', 'count': 'students'})
print(anxiety_summary.to_string())
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=subset, x=gender_col, y='anxiety_numeric', estimator=np.mean, errorbar=None, color='mediumpurple', ax=ax)
ax.set(xlabel='Gender', ylabel='Proportion Reporting Anxiety', title='Proportion Reporting Anxiety by Gender', ylim=(0, 1))
fig.tight_layout()
fig.savefig(RESULTS / 'exercise5_anxiety_by_gender.png', dpi=160)
plt.close(fig)

print('\nEXERCISE 6: Age and panic attacks')
subset2 = df[[age_col, panic_col]].copy()
subset2['age_numeric'] = pd.to_numeric(subset2[age_col], errors='coerce')
subset2['panic_numeric'] = subset2[panic_col].astype(str).str.strip().str.lower().map({'yes': 1, 'no': 0})
subset2 = subset2.dropna(subset=['age_numeric', 'panic_numeric'])
if subset2.empty:
    raise ValueError('No valid age / panic attack response pairs were found.')
print(subset2.groupby('age_numeric')['panic_numeric'].agg(['mean', 'count']).to_string())
fig, ax = plt.subplots(figsize=(9, 5))
sns.scatterplot(data=subset2, x='age_numeric', y='panic_numeric', alpha=0.5, s=65, ax=ax)
ax.set(xlabel='Age (years)', ylabel='Panic Attacks (No=0, Yes=1)', title='Age and Reported Panic Attacks', yticks=[0, 1], ylim=(-0.2, 1.2))
fig.tight_layout()
fig.savefig(RESULTS / 'exercise6_age_panic_scatter.png', dpi=160)
plt.close(fig)

summary = f'''WEEK 5 DAY 4 - EXERCISES XP: VISUALIZATION SUMMARY

Exercise 1: Visualizations make comparisons, trends and unusual values easier to identify. A line plot is useful for ordered/time-series values.
Exercise 2: Weekly temperature peaked on Friday at {max(temperatures)} °F and was lowest on Monday at {min(temperatures)} °F.
Exercise 3: Sales increased from ${sales[0]:,} in January to ${sales[-1]:,} in May.
Exercise 4: Most frequent CGPA category: {cgpa.mode().iloc[0] if not cgpa.dropna().empty else 'Unavailable'}.
Exercise 5: Anxiety is reported as a proportion within each gender (not a raw count); this makes groups with different sample sizes comparable. These are self-reported survey responses.
Exercise 6: Scatter points at 0 and 1 show the reported absence/presence of panic attacks at each age. Overlapping points can hide repeated observations, and the chart does not establish causation.

Dataset: {len(df)} records; {len(df.columns)} columns.
Note: This is an observational student survey. Results are descriptive, not causal, and may not generalize to all students.
'''
(RESULTS / 'analysis_summary.txt').write_text(summary, encoding='utf-8')
anxiety_summary.to_csv(RESULTS / 'anxiety_by_gender.csv')
print('\n' + summary)
print('Saved five charts, summary, and anxiety table to:', RESULTS)
