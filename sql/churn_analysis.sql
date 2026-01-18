-- ===============================
-- CUSTOMER CHURN ANALYSIS (SQL)
-- ===============================

-- Assumption:
-- Table name: churn_data
-- Columns follow Telco Churn dataset naming

------------------------------------------------
-- 1. Overall churn rate
------------------------------------------------
SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS churn_rate_percent
FROM churn_data;

------------------------------------------------
-- 2. Churn by contract type
------------------------------------------------
SELECT
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS churn_rate_percent
FROM churn_data
GROUP BY Contract
ORDER BY churn_rate_percent DESC;

------------------------------------------------
-- 3. Churn by payment method
------------------------------------------------
SELECT
    PaymentMethod,
    COUNT(*) AS total_customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS churn_rate_percent
FROM churn_data
GROUP BY PaymentMethod
ORDER BY churn_rate_percent DESC;

------------------------------------------------
-- 4. Average charges by churn status
------------------------------------------------
SELECT
    Churn,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges,
    ROUND(AVG(TotalCharges), 2) AS avg_total_charges
FROM churn_data
GROUP BY Churn;

------------------------------------------------
-- 5. Tenure bucket churn analysis
------------------------------------------------
SELECT
    CASE
        WHEN tenure < 12 THEN '0–12 months'
        WHEN tenure BETWEEN 12 AND 24 THEN '12–24 months'
        WHEN tenure BETWEEN 25 AND 48 THEN '25–48 months'
        ELSE '48+ months'
    END AS tenure_group,
    COUNT(*) AS customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS churn_rate_percent
FROM churn_data
GROUP BY tenure_group
ORDER BY churn_rate_percent DESC;

------------------------------------------------
-- 6. High-value customers at churn risk
------------------------------------------------
SELECT
    Contract,
    COUNT(*) AS high_value_customers,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges
FROM churn_data
WHERE Churn = 'Yes'
  AND MonthlyCharges > (
      SELECT AVG(MonthlyCharges) FROM churn_data
  )
GROUP BY Contract
ORDER BY high_value_customers DESC;
