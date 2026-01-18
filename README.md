Customer Churn Analysis & Prediction

About the Project
This project focuses on understanding customer churn and identifying customers who are at high risk of leaving a service.
The goal was to approach churn from a business and analytics perspective, not just build a machine learning model.
The analysis answers questions such as:
Why do customers churn?
Which customers are more likely to churn?
How can the business reduce churn using data-driven insights?

Dataset
Source: Telco Customer Churn Dataset (Kaggle)
Type: Customer-level data
Target variable: Churn (Yes / No)
Key features include:
Customer tenure
Monthly and total charges
Contract type
Payment method
Service subscriptions

Project Workflow
1. Data Validation
The raw dataset was checked for:
Missing values
Incorrect data types (especially billing fields)
Valid churn labels
Some numeric fields required cleaning before analysis.
Script: 01_data_validation.py
Output: outputs/churn_clean.csv
2. Exploratory Data Analysis
Exploratory analysis was done to understand churn patterns:
Churn rate distribution
Tenure comparison between churned and retained customers
Monthly charges vs churn
Churn behavior across contract types and payment methods
This step helped identify key churn drivers before modeling.
Script: 02_exploratory_analysis.py
3. Feature Engineering
To prepare the data for modeling:
Churn was converted to a binary target variable
Non-informative identifiers were removed
Categorical variables were one-hot encoded
This resulted in a clean, model-ready dataset.
Script: 03_feature_engineering.py
Output: outputs/churn_features.csv
4. Churn Model Building
A Logistic Regression model was used to predict churn probability because:
It is interpretable
It produces probability scores useful for business decisions
The dataset was split into training and testing sets using stratification.
Script: 04_churn_model.py
Output: outputs/churn_predictions.csv
5. Model Evaluation
The model was evaluated using:
Accuracy
Precision
Recall
ROC–AUC score
ROC–AUC was treated as the key metric since identifying churners is more important than overall accuracy.
A ROC curve was plotted to visualize performance.
Script: 05_model_evaluation.py
6. Business Insights & Recommendations
Predicted churn probabilities were converted into risk segments:
Low Risk
Medium Risk
High Risk
Based on the results, practical recommendations were suggested, such as:
Targeting high-risk customers with retention offers
Encouraging long-term contracts
Reviewing pricing for high monthly charge customers
Script: 06_business_insights.py
Output: outputs/churn_risk_segments.csv

## SQL Analysis
Along with Python-based modeling, SQL was used to analyze churn patterns such as:
- Overall churn rate
- Churn by contract type and payment method
- Tenure-based churn segmentation
- High-value churned customers

These queries simulate real-world analysis on customer tables stored in relational databases.


Tools Used
Python
pandas
scikit-learn
matplotlib

Key Learnings
Customer tenure and contract type strongly influence churn
Month-to-month customers are significantly more likely to churn
Probability-based models are more useful than binary predictions
Translating model outputs into business actions is critical

How to Run the Project

pip3 install pandas matplotlib scikit-learn

python3 01_data_validation.py

python3 02_exploratory_analysis.py

python3 03_feature_engineering.py

python3 04_churn_model.py

python3 05_model_evaluation.py

python3 06_business_insights.py

Interview Summary (Short)
Built a customer churn analytics pipeline that analyzed churn drivers, trained a logistic regression model to predict churn risk, evaluated model performance, and translated predictions into actionable business recommendations.

Possible Improvements
Try tree-based models (Random Forest, XGBoost)
Tune classification threshold for better recall
Integrate churn predictions into a dashboard
Perform cohort-based churn analysis
