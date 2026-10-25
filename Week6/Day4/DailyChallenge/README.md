# Week 6 Day 4 — Global Power Plant Analysis

## Assignment
Analyze the Global Power Plant Database using NumPy, Pandas, Matplotlib, Seaborn, and SciPy.

## Deliverables
- `Week6_Day4_DailyChallenge.ipynb` — complete notebook with cleaning, EDA, hypothesis testing, time series, geography, matrix eigendecomposition, charts, and a dynamically generated executive summary.
- `results/` — generated plots, cleaned dataset, grouped statistics, and analysis report after running all notebook cells.

## Dataset
World Resources Institute Global Power Plant Database v1.3.0, via the dataset ZIP linked in the assignment. Download is attempted automatically; a ZIP or CSV placed beside the notebook is also supported.

## Run
```powershell
py -m pip install numpy pandas matplotlib seaborn scipy jupyter ipykernel
```
Open the notebook in Jupyter or PyCharm, select **Run All**, and save it before committing.

## Key findings
After execution, use the actual computed figures in `results/analysis_report.md`. The notebook calculates the leading country and fuel type, total installed capacity, a fuel-type Welch t-test, historical fuel mix, and geographic patterns. **No findings are asserted here before running the dataset.**

## Limitations
Installed capacity (MW) is not electricity generation. Missing commissioning years and coordinates can bias analysis; the geographical visualization is a coordinate scatterplot. Correlation does not imply causation.
