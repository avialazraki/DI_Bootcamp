
import pandas as pd
from pathlib import Path

# Exercise 2: Dataset Loading and Initial Analysis

# Get the folder where this Python file is located
folder = Path(__file__).resolve().parent

# Load the Sleep dataset
sleep_df = pd.read_csv(folder / "Time Americans Spend Sleeping.csv")

# Display the first five rows
print("=== HOW MUCH SLEEP DO AMERICANS GET? ===")
print(sleep_df.head())

# Display dataset information
print("\nDataset shape (rows, columns):")
print(sleep_df.shape)

print("\nColumn names:")
print(sleep_df.columns.tolist())

print("\nDataset information:")
sleep_df.info()


# Exercise 2: Global Trends in Mental Health Disorder

mental_health_df = pd.read_csv(
    folder / "Mental health Depression disorder Data.csv"
)

print("\n=== GLOBAL TRENDS IN MENTAL HEALTH DISORDER ===")

# Display the first five rows
print(mental_health_df.head())

# Display dataset dimensions
print("\nDataset shape (rows, columns):")
print(mental_health_df.shape)

# Display column names
print("\nColumn names:")
print(mental_health_df.columns.tolist())

# Display dataset information
print("\nDataset information:")
mental_health_df.info()


# Exercise 2: Credit Card Approvals Dataset

credit_df = pd.read_csv(folder / "clean_dataset.csv")

print("\n=== CREDIT CARD APPROVALS ===")

# Display the first five rows
print(credit_df.head())

# Display dataset dimensions
print("\nDataset shape (rows, columns):")
print(credit_df.shape)

# Display column names
print("\nColumn names:")
print(credit_df.columns.tolist())

# Display dataset information
print("\nDataset information:")
credit_df.info()


# Exercise 2: Brief Dataset Descriptions

print("\n=== DATASET DESCRIPTIONS ===")

print("""
1. HOW MUCH SLEEP DO AMERICANS REALLY GET?
This dataset contains 945 records and 9 columns.
It provides information about average daily sleeping hours
across different years, age groups, sexes, and types of days.
It can be used to analyze sleeping patterns and compare groups.
All columns have complete data.

2. GLOBAL TRENDS IN MENTAL HEALTH DISORDER
This dataset contains 108,553 records and 11 columns.
It includes country or region information, years, and
measurements related to different mental health disorders.
It can be used to study geographical and historical trends.
Several columns contain missing values, and some have
mixed data types that may require cleaning.

3. CREDIT CARD APPROVALS
This dataset contains 690 records and 16 columns.
It includes applicant characteristics such as age,
employment, income, credit score, and approval status.
It can be used to explore factors associated with
credit card approval decisions.
All columns have complete data.
""")
