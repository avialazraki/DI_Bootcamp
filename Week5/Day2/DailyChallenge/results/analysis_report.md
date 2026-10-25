# Week 5 Day 2 — Daily Challenge: Airplane Crash Analysis

## 1. Data and cleaning
Source: https://github.com/devtlv/Datasets-DA-Bootcamp-2-/raw/refs/heads/main/W4%20Gen%20AI/W4D3/Airplane%20Crashes%20and%20Fatalities%20upto%202023.zip
Original records: 4,998; retained dated records through 2023: 4,998.
Records with known onboard fatalities: 4,990.
Records with calculable onboard survival rates: 4,975.
Converted dates and numeric columns, removed exact duplicates, handled missing data,
and excluded impossible onboard fatality counts greater than aboard counts.
Unknown fatalities or passenger counts remain missing rather than being assumed zero.

## 2. Exploratory data analysis
Recorded crashes: 4,998.
Sum of known onboard fatalities: 111,644.
Mean fatalities per crash with known fatalities: 22.37.
Median fatalities per crash with known fatalities: 11.00.
Standard deviation of fatalities (sample): 35.06.
Mean of incident-level survival rates: 18.15%.
Median incident-level survival rate: 0.00%.
Standard deviation of incident-level survival rates: 0.3117.
Year with most recorded crashes: 1946 (88).

## 3. Statistical hypothesis test
Null hypothesis: mean onboard fatalities per recorded crash are equal in the two compared decades.
Alternative hypothesis: these means differ.
Welch t-test: 2010s vs 2020s; n=235 vs 27; means=27.26 vs 30.78; t=-0.4006; p=0.691267. Insufficient evidence of different mean fatalities per recorded crash (p >= 0.05).
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
The peak year is 1946 in this recorded dataset.
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
