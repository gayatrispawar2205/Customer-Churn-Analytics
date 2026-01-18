import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve
)

# -----------------------------
# Load predictions
# -----------------------------
df = pd.read_csv("outputs/churn_predictions.csv")

y_true = df['Actual_Churn']
y_prob = df['Churn_Probability']

# Default threshold
y_pred = (y_prob >= 0.5).astype(int)

# -----------------------------
# Evaluation metrics
# -----------------------------
print("\n--- Model Evaluation ---")
print("Accuracy :", round(accuracy_score(y_true, y_pred), 3))
print("Precision:", round(precision_score(y_true, y_pred), 3))
print("Recall   :", round(recall_score(y_true, y_pred), 3))
print("ROC-AUC  :", round(roc_auc_score(y_true, y_prob), 3))

# -----------------------------
# ROC Curve
# -----------------------------
fpr, tpr, _ = roc_curve(y_true, y_prob)

plt.figure(figsize=(6,5))
plt.plot(fpr, tpr, label="Logistic Regression")
plt.plot([0,1], [0,1], linestyle='--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Churn Model")
plt.legend()
plt.tight_layout()
plt.show()

print("\n✅ Model evaluation complete.")
