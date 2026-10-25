# Week 5 Day 6 — Interactive Data Visualization Daily Challenge

## Objective
Analyze US Superstore sales with interactive Matplotlib, a geographic Plotly map, and Seaborn product and discount/profit charts.

## Notebook
[Open the complete notebook](Week5_Day6_DailyChallenge.ipynb)

## How to run
1. Install `pandas numpy matplotlib seaborn xlrd ipywidgets plotly requests jupyter ipykernel`.
2. Open the notebook in Jupyter and run all cells. The notebook downloads the US Superstore Excel dataset automatically, or uses a local `US Superstore data.xls` file.
3. Save the executed notebook before committing. Interactive widgets need a running Jupyter kernel; GitHub previews show static saved outputs only.

## Key insights (fill from the executed notebook)
- **Revenue and profit:** See the calculated executive summary in Section 7.
- **Geography:** See the highest-sales state in Section 7 and the interactive state map. The source dataset may include only the United States, so cross-country comparisons are limited.
- **Products:** See the leading product and the top-ten sales chart in Section 4.
- **Discounts:** Compare observed loss rates for discounts above 20% and at or below 20% in Section 7. Correlation does not establish causation.

## Marketing recommendations
- Prioritize regions based on both sales and profitability, not revenue alone.
- Investigate high-discount, loss-making orders by product category.
- Use interactive charts to explore trends and Seaborn charts for executive communication.

**Note:** The bullet points above are intentionally qualitative until the notebook is executed on the dataset. Replace them with calculated values from Section 7 before final submission.
