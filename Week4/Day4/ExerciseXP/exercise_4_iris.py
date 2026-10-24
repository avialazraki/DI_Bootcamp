
import pandas as pd
from pathlib import Path

# Exercise 4: Identifying Data Types in the Iris Dataset

folder = Path(__file__).resolve().parent

# Load the Iris dataset
iris_df = pd.read_csv(folder / "Iris.csv")

print("=== IRIS DATASET ===")

# Display the first five rows
print(iris_df.head())

# Display dataset dimensions
print("\nDataset shape (rows, columns):")
print(iris_df.shape)

# Display column names
print("\nColumn names:")
print(iris_df.columns.tolist())

# Display data types and missing values
print("\nDataset information:")
iris_df.info()
