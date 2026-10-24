
import pandas as pd
from pathlib import Path

# Exercise 10: Importing JSON Data with Pandas

folder = Path(__file__).resolve().parent

# Load the JSON dataset
posts_df = pd.read_json(folder / "posts.json")

print("=== POSTS JSON DATASET ===")

# Display the first five rows
print(posts_df.head())

# Display dataset dimensions
print("\nDataset shape (rows, columns):")
print(posts_df.shape)

# Display column names
print("\nColumn names:")
print(posts_df.columns.tolist())

# Display dataset information
print("\nDataset information:")
posts_df.info()
