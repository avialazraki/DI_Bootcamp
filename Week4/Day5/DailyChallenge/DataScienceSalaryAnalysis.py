
# ==============================================
# Week 4 - Day 5 - Daily Challenge
# Data Handling and Analysis in Python
# ==============================================

import io
import zipfile
from pathlib import Path
from urllib.request import urlopen

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, StandardScaler


# ----------------------------------------------
# 1. Load the dataset
# ----------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "results"
OUTPUT_DIR.mkdir(exist_ok=True)

DATASET_URL = (
    "https://github.com/devtlv/"
    "Datasets-DA-Bootcamp-2-/raw/refs/heads/main/"
    "Week%204%20-%20Data%20Understanding/"
    "W4D4%20-%20Data%20Preprocessing%20%26%20T/"
    "Data%20Science%20Job%20Salary%20dataset.zip"
)


def load_dataset():
    local_zip = BASE_DIR / "Data Science Job Salary dataset.zip"

    if local_zip.exists():
        print("Loading local ZIP dataset...")
        zip_bytes = local_zip.read_bytes()
    else:
        print("Downloading dataset from GitHub...")
        try:
            with urlopen(DATASET_URL, timeout=30) as response:
                zip_bytes = response.read()
        except Exception as error:
            raise RuntimeError(
                "Download failed. Download the ZIP from the "
                "assignment link and save it beside this script."
            ) from error

    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as archive:
        csv_files = sorted(
            name for name in archive.namelist()
            if name.lower().endswith(".csv")
            and not Path(name).name.startswith("._")
        )

        if not csv_files:
            raise ValueError("No CSV file found inside ZIP.")

        print("Reading:", csv_files[0])

        with archive.open(csv_files[0]) as file:
            return pd.read_csv(file)


df = load_dataset()

print("\nDATASET OVERVIEW")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())
print("\nMissing values:")
print(df.isna().sum())


# ----------------------------------------------
# 2. Clean the dataset
# ----------------------------------------------

df.columns = df.columns.str.strip().str.lower()

df = df.drop_duplicates().copy()

required_columns = ["salary", "experience_level"]

for column in required_columns:
    if column not in df.columns:
        raise ValueError(f"Missing required column: {column}")

df["salary"] = pd.to_numeric(
    df["salary"], errors="coerce"
)

if "salary_in_usd" in df.columns:
    df["salary_in_usd"] = pd.to_numeric(
        df["salary_in_usd"], errors="coerce"
    )

df["experience_level"] = (
    df["experience_level"].astype("string").str.strip()
)

df = df.dropna(
    subset=["salary", "experience_level"]
).copy()

print("\nRows after cleaning:", len(df))

if df.empty:
    raise ValueError("No usable rows remain after cleaning.")


# ----------------------------------------------
# 3. Min-Max normalize salary
# ----------------------------------------------

scaler = MinMaxScaler()

df["salary_normalized"] = scaler.fit_transform(
    df[["salary"]]
).ravel()

print("\nSALARY NORMALIZATION")
print(
    df[["salary", "salary_normalized"]].head(10)
)

print(
    "Normalized minimum:",
    df["salary_normalized"].min()
)

print(
    "Normalized maximum:",
    df["salary_normalized"].max()
)


# ----------------------------------------------
# 4. Aggregate salaries by experience level
# ----------------------------------------------

# Use USD for comparisons when available.
salary_column = (
    "salary_in_usd"
    if "salary_in_usd" in df.columns
    else "salary"
)

experience_labels = {
    "EN": "Entry-level",
    "MI": "Mid-level",
    "SE": "Senior-level",
    "EX": "Executive-level"
}

df["experience_label"] = (
    df["experience_level"]
    .replace(experience_labels)
)

salary_stats = (
    df.groupby("experience_label")[salary_column]
    .agg(
        count="count",
        average_salary="mean",
        median_salary="median"
    )
    .round(2)
    .sort_values("average_salary")
)

print("\nSALARY STATISTICS BY EXPERIENCE")
print("Salary column:", salary_column)
print(salary_stats)

salary_stats.to_csv(
    OUTPUT_DIR / "salary_by_experience.csv"
)


# ----------------------------------------------
# 5. Dimensionality reduction using PCA
# ----------------------------------------------

# Select meaningful features available in
# the dataset. One-hot encode categories.

numeric_features = [
    column for column in [
        "work_year",
        "remote_ratio",
        "salary_normalized"
    ]
    if column in df.columns
]

categorical_features = [
    column for column in [
        "experience_level",
        "employment_type",
        "company_size"
    ]
    if column in df.columns
]

features = df[
    numeric_features + categorical_features
].copy()

for column in numeric_features:
    features[column] = pd.to_numeric(
        features[column], errors="coerce"
    )

    features[column] = features[column].fillna(
        features[column].median()
    )

for column in categorical_features:
    features[column] = (
        features[column].fillna("Unknown")
    )

features = pd.get_dummies(
    features,
    columns=categorical_features,
    dtype=int
)

# Remove constant features that contain
# no variation.
features = features.loc[
    :, features.nunique() > 1
]

if len(df) < 2 or features.shape[1] < 2:
    raise ValueError(
        "PCA needs at least two rows and "
        "two varying features."
    )

standard_scaler = StandardScaler()

scaled_features = standard_scaler.fit_transform(
    features
)

pca = PCA(n_components=2)

pca_result = pca.fit_transform(
    scaled_features
)

df["PCA1"] = pca_result[:, 0]
df["PCA2"] = pca_result[:, 1]

explained_variance = (
    pca.explained_variance_ratio_
)

print("\nPCA RESULTS")
print("Original feature count:", features.shape[1])
print("Reduced feature count:", 2)

print(
    "Explained variance ratio:",
    explained_variance
)

print(
    "Total explained variance:",
    explained_variance.sum()
)


# ----------------------------------------------
# 6. Visualization: Average and median salary
# ----------------------------------------------

ax = salary_stats[
    ["average_salary", "median_salary"]
].plot(
    kind="bar",
    figsize=(10, 6)
)

ax.set_title(
    "Average and Median Salary by Experience Level"
)
ax.set_xlabel("Experience Level")
ax.set_ylabel(
    "Salary (USD)"
    if salary_column == "salary_in_usd"
    else "Salary (original currency units)"
)

plt.xticks(rotation=25)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "salary_by_experience.png",
    dpi=150
)
plt.close()


# ----------------------------------------------
# 7. Visualization: PCA
# ----------------------------------------------

plt.figure(figsize=(10, 6))

for level, group in df.groupby("experience_label"):
    plt.scatter(
        group["PCA1"],
        group["PCA2"],
        label=level,
        alpha=0.5,
        s=18
    )

plt.title("PCA - Data Science Salary Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "pca_visualization.png",
    dpi=150
)
plt.close()


# ----------------------------------------------
# 8. Save processed dataset
# ----------------------------------------------

df.to_csv(
    OUTPUT_DIR / "processed_salary_data.csv",
    index=False
)


# ----------------------------------------------
# 9. Generate insights summary
# ----------------------------------------------

highest_level = salary_stats[
    "average_salary"
].idxmax()

lowest_level = salary_stats[
    "average_salary"
].idxmin()

summary = f"""
WEEK 4 DAY 5 - DAILY CHALLENGE
DATA HANDLING AND ANALYSIS

1. DATA CLEANING

The dataset was loaded from a ZIP file.
Duplicate records and rows with missing
required values were removed.

Final dataset size: {len(df)} rows.

2. MIN-MAX NORMALIZATION

The original salary column was normalized
using MinMaxScaler.

Normalized minimum:
{df['salary_normalized'].min():.4f}

Normalized maximum:
{df['salary_normalized'].max():.4f}

3. DIMENSIONALITY REDUCTION

PCA reduced {features.shape[1]} encoded
features to 2 principal components.

Explained variance:
PC1: {explained_variance[0]:.2%}
PC2: {explained_variance[1]:.2%}
Combined: {explained_variance.sum():.2%}

4. SALARY ANALYSIS

Salary comparison column: {salary_column}

{salary_stats.to_string()}

Highest average salary group:
{highest_level}

Lowest average salary group:
{lowest_level}

5. CONCLUSION

Min-Max normalization placed salary values
on a consistent scale between 0 and 1.

PCA compressed multiple dataset features
into two components for visualization.

Salary aggregation revealed differences
in average and median compensation across
experience levels.

Note: PCA components are not necessarily
directly interpretable, and salary
differences do not establish causation.

If salary_in_usd was unavailable,
salary comparisons may mix currencies.
"""

summary_path = OUTPUT_DIR / "analysis_summary.txt"

summary_path.write_text(
    summary.strip() + "\n",
    encoding="utf-8"
)

print("\n" + summary)
print("\nAnalysis completed successfully!")
print("Results saved in:", OUTPUT_DIR)
