import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, t
from pathlib import Path

# -----------------------------
# Task 4: Hypothesis Testing
# -----------------------------
# Tests whether average transaction sales differ between
# Male and Female customers using Welch's t-test.

INPUT_FILE = Path("sales_dataset_cleaned.csv")
OUTPUT_DIR = Path("Task4_Hypothesis_Testing")
OUTPUT_DIR.mkdir(exist_ok=True)

# Load the cleaned dataset
df = pd.read_csv(INPUT_FILE)

# Validate required columns and analysis fields
required_columns = {"Gender", "Total_Sales"}
missing_columns = required_columns - set(df.columns)
if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")

if df[["Gender", "Total_Sales"]].isnull().any().any():
    raise ValueError("Missing values found in analysis columns.")

# Create the two comparison groups
male_sales = df.loc[df["Gender"].eq("Male"), "Total_Sales"].astype(float)
female_sales = df.loc[df["Gender"].eq("Female"), "Total_Sales"].astype(float)

# Descriptive statistics
male_n, female_n = len(male_sales), len(female_sales)
male_mean, female_mean = male_sales.mean(), female_sales.mean()
male_std, female_std = male_sales.std(ddof=1), female_sales.std(ddof=1)

# Welch's independent two-sample t-test
t_statistic, p_value = ttest_ind(
    male_sales, female_sales, equal_var=False
)

# Welch-Satterthwaite degrees of freedom
se = np.sqrt((male_std**2 / male_n) + (female_std**2 / female_n))
welch_df = (
    ((male_std**2 / male_n) + (female_std**2 / female_n)) ** 2
    / (
        ((male_std**2 / male_n) ** 2 / (male_n - 1))
        + ((female_std**2 / female_n) ** 2 / (female_n - 1))
    )
)

# 95% confidence interval for Male - Female mean difference
alpha = 0.05
mean_difference = male_mean - female_mean
critical_value = t.ppf(1 - alpha / 2, welch_df)
ci_lower = mean_difference - critical_value * se
ci_upper = mean_difference + critical_value * se

# Cohen's d effect size
pooled_std = np.sqrt(
    ((male_n - 1) * male_std**2 + (female_n - 1) * female_std**2)
    / (male_n + female_n - 2)
)
cohens_d = mean_difference / pooled_std

# Statistical decision
decision = "Reject H0" if p_value < alpha else "Do not reject H0"

print("TASK 4 — HYPOTHESIS TESTING")
print("-" * 50)
print(f"Male sample size: {male_n}")
print(f"Female sample size: {female_n}")
print(f"Male mean: ₹{male_mean:,.2f}")
print(f"Female mean: ₹{female_mean:,.2f}")
print(f"Mean difference: ₹{mean_difference:,.2f}")
print(f"t-statistic: {t_statistic:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"95% CI: ₹{ci_lower:,.2f} to ₹{ci_upper:,.2f}")
print(f"Cohen's d: {cohens_d:.4f}")
print(f"Decision: {decision}")
