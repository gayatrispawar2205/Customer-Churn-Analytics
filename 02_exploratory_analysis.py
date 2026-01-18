import pandas as pd

# -----------------------------
# Load clean churn data
# -----------------------------
df = pd.read_csv("outputs/churn_clean.csv")

print("Data shape:", df.shape)

# -----------------------------
# Overall churn rate
# -----------------------------
print("\n--- Churn Distribution ---")
print(df['Churn'].value_counts())
print("\nChurn percentage:")
print(df['Churn'].value_counts(normalize=True) * 100)

# -----------------------------
# Tenure vs churn
# -----------------------------
print("\n--- Average Tenure by Churn ---")
print(df.groupby('Churn')['tenure'].mean())

# -----------------------------
# Monthly charges vs churn
# -----------------------------
print("\n--- Average Monthly Charges by Churn ---")
print(df.groupby('Churn')['MonthlyCharges'].mean())

# -----------------------------
# Contract type vs churn
# -----------------------------
print("\n--- Churn by Contract Type ---")
print(
    df.groupby('Contract')['Churn']
    .value_counts(normalize=True)
    .unstack() * 100
)

# -----------------------------
# Payment method vs churn
# -----------------------------
print("\n--- Churn by Payment Method ---")
print(
    df.groupby('PaymentMethod')['Churn']
    .value_counts(normalize=True)
    .unstack() * 100
)

print("\n✅ Exploratory churn analysis complete.")
