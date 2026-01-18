import pandas as pd

# -----------------------------
# Load clean churn data
# -----------------------------
df = pd.read_csv("outputs/churn_clean.csv")

# -----------------------------
# Target variable encoding
# -----------------------------
df['Churn_Flag'] = df['Churn'].map({'Yes': 1, 'No': 0})

# -----------------------------
# Drop non-informative columns
# -----------------------------
df = df.drop(['customerID', 'Churn'], axis=1)

# -----------------------------
# One-hot encode categorical features
# -----------------------------
categorical_cols = df.select_dtypes(include=['object']).columns

df_encoded = pd.get_dummies(
    df,
    columns=categorical_cols,
    drop_first=True
)

print("Feature dataset shape:", df_encoded.shape)

# -----------------------------
# Save feature dataset
# -----------------------------
df_encoded.to_csv("outputs/churn_features.csv", index=False)

print("\n✅ Feature engineering complete.")
print("Saved to outputs/churn_features.csv")
