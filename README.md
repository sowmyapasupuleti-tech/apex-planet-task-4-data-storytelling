# Apex Planet Solutions – Task 4
## Sales Performance & Customer Insights

### 📌 Project Overview

This project is part of my Data Analytics Internship at Apex Planet Solutions Pvt Ltd.

The objective of Task 4 is to bring together the analysis performed in the previous tasks and present the findings as a clear business data story. The project combines exploratory data analysis, business insights, customer segmentation, correlation analysis, and statistical hypothesis testing.

---

## 🎯 Objectives

- Analyze overall sales performance.
- Identify high-performing products.
- Understand customer and age-segment patterns.
- Study relationships between sales and key numerical variables.
- Formulate and test a business hypothesis.
- Convert analytical findings into actionable business recommendations.
- Present the insights through a stakeholder-friendly presentation.

---

## 📊 Dataset

The analysis was performed on a cleaned sales dataset containing:

- **1,000 transactions**
- **12 columns**
- No missing values
- No duplicate rows

Important variables include:

- Order ID
- Order Date
- Customer ID
- Customer Name
- Age
- Gender
- City
- Product
- Category
- Quantity
- Unit Price
- Total Sales

---

## 📈 Key Business Insights

### Overall Performance

- **Total Sales:** ₹139.40M
- **Transactions:** 1,000
- **Average Quantity:** 5.44
- **Average Order Value:** ₹139.40K

### Product Performance

| Product | Total Sales |
|---|---:|
| Laptop | ₹25.44M |
| Mobile | ₹25.34M |
| Book | ₹25.03M |
| Rice | ₹22.23M |
| Chair | ₹21.52M |
| Shoes | ₹19.84M |

Laptop generated the highest total sales among the analyzed products.

### Customer Insights

Total sales by gender:

- **Male:** ₹72.46M
- **Female:** ₹66.94M

Although male customers generated higher observed total sales, this difference was further tested statistically rather than being treated as automatically meaningful.

### Age Segmentation

Customers were grouped into three age segments:

- **Young:** < 30
- **Adult:** 30–59
- **Senior:** ≥ 60

The Adult segment was the strongest contributor to sales.

---

## 📐 Correlation Analysis

Two important relationships were examined:

- **Quantity vs Total Sales:** r = 0.647
- **Unit Price vs Total Sales:** r = 0.686

Both relationships show positive association with Total Sales.

> Correlation indicates association and does not prove causation.

---

# 🧪 Hypothesis Testing

### Business Question

**Do average transaction sales differ between male and female customers?**

### Hypotheses

**Null Hypothesis (H₀):**

There is no statistically significant difference in average transaction sales between male and female customers.

**Alternative Hypothesis (H₁):**

There is a statistically significant difference in average transaction sales between male and female customers.

### Statistical Test

A **Welch's independent two-sample t-test** was used because the objective was to compare the mean sales of two independent groups.

- Significance level (α): **0.05**
- Confidence level: **95%**

### Results

| Metric | Result |
|---|---:|
| Male Mean Sales | ₹141,807.34 |
| Female Mean Sales | ₹136,883.21 |
| Mean Difference | ₹4,924.13 |
| t-statistic | 0.6826 |
| p-value | 0.4950 |
| Welch Degrees of Freedom | 997.98 |
| 95% Confidence Interval | −₹9,231.58 to ₹19,079.85 |
| Cohen's d | 0.0431 |

### Statistical Decision

Since:

**p-value = 0.4950 > 0.05**

we **do not reject the null hypothesis**.

### Business Interpretation

The analysis does not provide sufficient statistical evidence at the 5% significance level to conclude that average transaction sales differ between male and female customers.

The observed difference in sample means exists, but it is not statistically significant based on this test.

This analysis is observational, so the results should not be interpreted as evidence of causation.

---

## 💡 Business Recommendations

1. Focus on high-performing products such as laptops, mobiles, and books.
2. Use customer age segmentation to support targeted marketing strategies.
3. Monitor geographic and product-level performance to identify growth opportunities.
4. Avoid making strong marketing decisions based solely on observed gender differences.
5. Use controlled experiments or A/B testing when causal evidence is required.
6. Continue using statistical validation alongside descriptive analytics when evaluating business patterns.

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- SciPy
- Excel
- SQL
- Power BI
- Data Visualization
- Statistical Hypothesis Testing

---

## 📁 Project Structure

```text
Apex Planet Task 4/
│
├── Final_Presentation/
│   └── Sales_Performance_Customer_Insights.pptx
│
├── Hypothesis_Testing/
│   ├── hypothesis_testing.py
│   ├── hypothesis_testing_results.xlsx
│   ├── hypothesis_testing_summary.txt
│   └── hypothesis_boxplot.png
│
├── Visuals/
│
└── README.md
