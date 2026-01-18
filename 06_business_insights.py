import pandas as pd

# -----------------------------
# Load predictions
# -----------------------------
df = pd.read_csv("outputs/churn_predictions.csv")

# -----------------------------
# Define risk segments
# -----------------------------
df['Risk_Segment'] = pd.cut(
    df['Churn_Probability'],
    bins=[0, 0.3, 0.6, 1.0],
    labels=['Low Risk', 'Medium Risk', 'High Risk']
)

# -----------------------------
# Risk distribution
# -----------------------------
print("\n--- Churn Risk Distribution ---")
print(df['Risk_Segment'].value_counts())

# -----------------------------
# High-risk customers
# -----------------------------
high_risk = df[df['Risk_Segment'] == 'High Risk']

print("\nHigh-risk customer count:", len(high_risk))
print("Average churn probability (high-risk):",
      round(high_risk['Churn_Probability'].mean(), 3))

# -----------------------------
# Business recommendations
# -----------------------------
print("\n--- Business Recommendations ---")
print("1. Target high-risk customers with retention offers.")
print("2. Incentivize long-term contracts over month-to-month plans.")
print("3. Review pricing for high monthly charge segments.")
print("4. Improve payment experience for electronic check users.")

# -----------------------------
# Save insights
# -----------------------------
df.to_csv("outputs/churn_risk_segments.csv", index=False)

print("\n✅ Business insights generation complete.")
print("Saved to outputs/churn_risk_segments.csv")
