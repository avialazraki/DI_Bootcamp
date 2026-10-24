
import pandas as pd
from pathlib import Path

# Exercise 9: Exporting Data to Excel and JSON

folder = Path(__file__).resolve().parent

# Create a sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 28, 35],
    "City": ["Tel Aviv", "Haifa", "Jerusalem", "Eilat"],
    "Salary": [12000, 15000, 13500, 18000]
}

df = pd.DataFrame(data)

print("=== SAMPLE DATAFRAME ===")
print(df)

# Export to Excel
df.to_excel(folder / "exercise_9_data.xlsx", index=False)

# Export to JSON
df.to_json(folder / "exercise_9_data.json",
           orient="records", indent=4)

print("\nData exported successfully!")
print("Created: exercise_9_data.xlsx")
print("Created: exercise_9_data.json")
