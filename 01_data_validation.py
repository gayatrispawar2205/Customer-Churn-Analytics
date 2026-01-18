import pandas as pd

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv("data/churn.csv")
df.columns = df.columns.str.strip()

print("Initial shape:", df.shape)

# -----------------------------
# Check target variable
# -----------------------------
print("\nChurn value counts:")
print(df['Churn'].value_counts())

# -----------------------------
# Convert TotalCharges to numeric
# -----------------------------
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

missing_total = df['TotalCharges'].isna().sum()
print("\nMissing TotalCharges:", missing_total)

df = df.dropna(subset=['TotalCharges'])

# -----------------------------
# Basic sanity checks
# -----------------------------
print("\nTenure summary:")
print(df['tenure'].describe())

print("\nMonthlyCharges summary:")
print(df['MonthlyCharges'].describe())

# -----------------------------
# Save clean data
# -----------------------------
df.to_csv("outputs/churn_clean.csv", index=False)

print("\n✅ Data validation complete.")
print("Saved to outputs/churn_clean.csv")
