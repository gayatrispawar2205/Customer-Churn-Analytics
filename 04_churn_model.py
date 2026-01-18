import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# -----------------------------
# Load feature dataset
# -----------------------------
df = pd.read_csv("outputs/churn_features.csv")

# -----------------------------
# Split features and target
# -----------------------------
X = df.drop('Churn_Flag', axis=1)
y = df['Churn_Flag']

# -----------------------------
# Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# -----------------------------
# Train Logistic Regression
# -----------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# -----------------------------
# Predict churn probability
# -----------------------------
y_prob = model.predict_proba(X_test)[:, 1]

# -----------------------------
# Save predictions
# -----------------------------
pred_df = X_test.copy()
pred_df['Actual_Churn'] = y_test.values
pred_df['Churn_Probability'] = y_prob

pred_df.to_csv("outputs/churn_predictions.csv", index=False)

print("\n✅ Churn model training complete.")
print("Saved predictions to outputs/churn_predictions.csv")
