
import pandas as pd
from pathlib import Path

# Exercise 8: Loading the Titanic Dataset

folder = Path(__file__).resolve().parent

# Load the Titanic CSV file
titanic_df = pd.read_csv(folder / "train.csv")

print("=== TITANIC DATASET ===")

# Display the first five rows
print(titanic_df.head())

# Display dataset dimensions
print("\nDataset shape (rows, columns):")
print(titanic_df.shape)

# Display column names
print("\nColumn names:")
print(titanic_df.columns.tolist())
