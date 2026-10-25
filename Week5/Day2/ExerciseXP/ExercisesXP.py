
# ==================================================
# WEEK 5 - DAY 2 - EXERCISES XP
# Statistical Analysis Using SciPy
# Exercises 1-8 (including optional exercises)
# ==================================================

from pathlib import Path

import scipy
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm, binom

# Save charts in the same assignment folder
BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)

# Reproducible random results
rng = np.random.default_rng(42)


# ==================================================
# EXERCISE 1: BASIC USAGE OF SCIPY
# ==================================================

print("\n" + "=" * 55)
print("EXERCISE 1: BASIC USAGE OF SCIPY")
print("=" * 55)

print("SciPy version:", scipy.__version__)


# ==================================================
# EXERCISE 2: DESCRIPTIVE STATISTICS
# ==================================================

print("\n" + "=" * 55)
print("EXERCISE 2: DESCRIPTIVE STATISTICS")
print("=" * 55)

data = np.array([12, 15, 13, 12, 18, 20, 22, 21])

mean = np.mean(data)
median = np.median(data)
variance = np.var(data, ddof=1)
std_dev = np.std(data, ddof=1)

description = stats.describe(data)

print("Dataset:", data.tolist())
print(f"Mean: {mean:.2f}")
print(f"Median: {median:.2f}")
print(f"Sample variance: {variance:.2f}")
print(f"Sample standard deviation: {std_dev:.2f}")

print("\nSciPy descriptive statistics:")
print(description)

print(
    "\nInterpretation: The mean describes the average, "
    "the median describes the middle value, and "
    "variance and standard deviation describe spread."
)


# ==================================================
# EXERCISE 3: UNDERSTANDING DISTRIBUTIONS
# ==================================================

print("\n" + "=" * 55)
print("EXERCISE 3: NORMAL DISTRIBUTION")
print("=" * 55)

mu = 50
sigma = 10

x = np.linspace(10, 90, 500)
y = norm.pdf(x, loc=mu, scale=sigma)

print("Mean:", mu)
print("Standard deviation:", sigma)

print(
    "Probability of a value between 40 and 60:",
    round(
        norm.cdf(60, mu, sigma)
        - norm.cdf(40, mu, sigma),
        4
    )
)

plt.figure(figsize=(9, 5))
plt.plot(x, y, label="Normal distribution")
plt.axvline(mu, linestyle="--", label="Mean = 50")
plt.title("Normal Distribution (Mean=50, SD=10)")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(
    RESULTS_DIR / "exercise3_normal_distribution.png",
    dpi=150
)
plt.close()

print("Normal distribution chart saved.")


# ==================================================
# EXERCISE 4: T-TEST APPLICATION
# ==================================================

print("\n" + "=" * 55)
print("EXERCISE 4: INDEPENDENT T-TEST")
print("=" * 55)

data1 = rng.normal(50, 10, 100)
data2 = rng.normal(60, 10, 100)

# Welch's independent-samples T-test
t_stat, p_value = stats.ttest_ind(
    data1, data2, equal_var=False
)

print(f"Group 1 mean: {np.mean(data1):.2f}")
print(f"Group 2 mean: {np.mean(data2):.2f}")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.8f}")

if p_value < 0.05:
    print(
        "Conclusion: Reject the null hypothesis. "
        "There is a statistically significant "
        "difference between the group means."
    )
else:
    print(
        "Conclusion: Fail to reject the null "
        "hypothesis. There is insufficient "
        "evidence of a difference."
    )

plt.figure(figsize=(8, 5))
plt.boxplot(
    [data1, data2],
    tick_labels=["Group 1", "Group 2"]
)
plt.title("T-Test: Comparison of Two Groups")
plt.ylabel("Values")
plt.tight_layout()
plt.savefig(
    RESULTS_DIR / "exercise4_ttest.png",
    dpi=150
)
plt.close()


# ==================================================
# EXERCISE 5: LINEAR REGRESSION
# ==================================================

print("\n" + "=" * 55)
print("EXERCISE 5: LINEAR REGRESSION")
print("=" * 55)

house_sizes = np.array([50, 70, 80, 100, 120])
house_prices = np.array([
    150000, 200000, 210000, 250000, 280000
])

regression = stats.linregress(
    house_sizes, house_prices
)

slope = regression.slope
intercept = regression.intercept
r_squared = regression.rvalue ** 2

predicted_price = slope * 90 + intercept

print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")
print(f"R-squared: {r_squared:.4f}")

print(
    f"Predicted price for a 90 m² house: "
    f"{predicted_price:,.2f}"
)

print(
    f"\nInterpretation: Each additional square "
    f"meter is associated with an estimated "
    f"increase of {slope:,.2f} currency units "
    f"in the house price."
)

print(
    f"Regression equation: "
    f"Price = {slope:.2f} * Size + {intercept:.2f}"
)

plt.figure(figsize=(9, 5))
plt.scatter(
    house_sizes,
    house_prices,
    label="Actual house prices"
)

x_line = np.linspace(
    house_sizes.min(),
    house_sizes.max(),
    100
)

plt.plot(
    x_line,
    slope * x_line + intercept,
    label="Regression line"
)

plt.scatter(
    [90],
    [predicted_price],
    marker="x",
    s=120,
    label="Prediction for 90 m²"
)

plt.title("House Size vs. House Price")
plt.xlabel("House Size (m²)")
plt.ylabel("House Price")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(
    RESULTS_DIR / "exercise5_linear_regression.png",
    dpi=150
)
plt.close()


# ==================================================
# EXERCISE 6: ANOVA
# ==================================================

print("\n" + "=" * 55)
print("EXERCISE 6: ONE-WAY ANOVA")
print("=" * 55)

fertilizer_1 = [5, 6, 7, 6, 5]
fertilizer_2 = [7, 8, 7, 9, 8]
fertilizer_3 = [4, 5, 4, 3, 4]

f_stat, anova_p = stats.f_oneway(
    fertilizer_1,
    fertilizer_2,
    fertilizer_3
)

print(f"F-statistic: {f_stat:.4f}")
print(f"P-value: {anova_p:.8f}")

print("\nAverage growth:")
print(
    f"Fertilizer 1: "
    f"{np.mean(fertilizer_1):.2f} cm"
)
print(
    f"Fertilizer 2: "
    f"{np.mean(fertilizer_2):.2f} cm"
)
print(
    f"Fertilizer 3: "
    f"{np.mean(fertilizer_3):.2f} cm"
)

if anova_p < 0.05:
    print(
        "\nConclusion: Reject the null hypothesis. "
        "At least one fertilizer group has a "
        "significantly different mean growth."
    )
else:
    print(
        "\nConclusion: Fail to reject the null "
        "hypothesis. There is insufficient "
        "evidence that mean growth differs."
    )

print(
    "\nIf the P-value were greater than 0.05, "
    "we would not have enough statistical "
    "evidence to conclude that the fertilizers "
    "have different mean effects."
)

print(
    "ANOVA does not identify which groups "
    "differ; a post-hoc test would be needed."
)

plt.figure(figsize=(8, 5))
plt.boxplot(
    [fertilizer_1, fertilizer_2, fertilizer_3],
    tick_labels=[
        "Fertilizer 1",
        "Fertilizer 2",
        "Fertilizer 3"
    ]
)
plt.title("Plant Growth by Fertilizer")
plt.ylabel("Growth (cm)")
plt.tight_layout()
plt.savefig(
    RESULTS_DIR / "exercise6_anova.png",
    dpi=150
)
plt.close()


# ==================================================
# EXERCISE 7: BINOMIAL DISTRIBUTION (OPTIONAL)
# ==================================================

print("\n" + "=" * 55)
print("EXERCISE 7: BINOMIAL DISTRIBUTION")
print("=" * 55)

n = 10
probability_of_heads = 0.5
exactly_five = binom.pmf(
    5, n, probability_of_heads
)

print(
    "Probability of exactly 5 heads "
    f"in 10 flips: {exactly_five:.4f}"
)

successes = np.arange(n + 1)
probabilities = binom.pmf(
    successes, n, probability_of_heads
)

for count, probability in zip(
    successes, probabilities
):
    print(
        f"{count} heads: "
        f"{probability:.4f}"
    )

plt.figure(figsize=(9, 5))
plt.bar(successes, probabilities)
plt.title(
    "Binomial Distribution: "
    "10 Fair Coin Flips"
)
plt.xlabel("Number of Heads")
plt.ylabel("Probability")
plt.xticks(successes)
plt.tight_layout()
plt.savefig(
    RESULTS_DIR / "exercise7_binomial.png",
    dpi=150
)
plt.close()


# ==================================================
# EXERCISE 8: CORRELATION (OPTIONAL)
# ==================================================

print("\n" + "=" * 55)
print("EXERCISE 8: CORRELATION")
print("=" * 55)

df = pd.DataFrame({
    "age": [23, 25, 30, 35, 40],
    "income": [
        35000, 40000, 50000, 60000, 70000
    ]
})

pearson_r, pearson_p = stats.pearsonr(
    df["age"], df["income"]
)

spearman_r, spearman_p = stats.spearmanr(
    df["age"], df["income"]
)

print("Dataset:")
print(df)

print(f"\nPearson correlation: {pearson_r:.4f}")
print(f"Pearson P-value: {pearson_p:.6f}")

print(
    f"Spearman correlation: "
    f"{spearman_r:.4f}"
)
print(
    f"Spearman P-value: "
    f"{spearman_p:.6f}"
)

print(
    "\nInterpretation: Both coefficients "
    "indicate a strong positive relationship "
    "between age and income in this example."
)

print(
    "Correlation does not prove causation, "
    "and the dataset contains only five records."
)

plt.figure(figsize=(8, 5))
plt.scatter(df["age"], df["income"])
plt.title("Age vs. Income")
plt.xlabel("Age")
plt.ylabel("Income")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(
    RESULTS_DIR / "exercise8_correlation.png",
    dpi=150
)
plt.close()


# ==================================================
# FINAL SUMMARY
# ==================================================

summary = f"""
WEEK 5 DAY 2 - EXERCISES XP
STATISTICAL ANALYSIS SUMMARY

Exercise 1: SciPy
SciPy version: {scipy.__version__}

Exercise 2: Descriptive Statistics
Mean: {mean:.2f}
Median: {median:.2f}
Sample variance: {variance:.2f}
Sample standard deviation: {std_dev:.2f}

Exercise 3: Normal Distribution
Mean: 50
Standard deviation: 10

Exercise 4: T-Test
T-statistic: {t_stat:.4f}
P-value: {p_value:.8f}
Significant at 0.05: {p_value < 0.05}

Exercise 5: Linear Regression
Slope: {slope:.2f}
Intercept: {intercept:.2f}
Predicted 90 m² price: {predicted_price:,.2f}
R-squared: {r_squared:.4f}

Exercise 6: ANOVA
F-statistic: {f_stat:.4f}
P-value: {anova_p:.8f}
Significant at 0.05: {anova_p < 0.05}

Exercise 7: Binomial Distribution
P(exactly 5 heads in 10 flips):
{exactly_five:.6f}

Exercise 8: Correlation
Pearson: {pearson_r:.4f}
Spearman: {spearman_r:.4f}

CONCLUSION

SciPy provides tools for statistical
description, probability distributions,
hypothesis testing, regression, ANOVA,
and correlation analysis.

Statistical significance is not the same
as practical importance or causation.
"""

(RESULTS_DIR / "analysis_summary.txt").write_text(
    summary.strip() + "\n",
    encoding="utf-8"
)

print("\n" + "=" * 55)
print("ALL 8 EXERCISES COMPLETED")
print("=" * 55)

print(summary)
print("Charts and summary saved to:")
print(RESULTS_DIR)
