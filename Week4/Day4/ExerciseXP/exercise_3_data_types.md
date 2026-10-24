
# Exercise 3: Identifying Data Types

## Dataset 1: How Much Sleep Do Americans Really Get?

| Column | Classification | Explanation |
|---|---|---|
| index | Identifier | Row number, not a measured quantity. |
| Year | Quantitative (discrete/time) | Numeric year used for chronological analysis. |
| Period | Qualitative | Describes the reporting period, such as Annual. |
| Avg hrs per day sleeping | Quantitative (continuous) | Measures average sleeping hours. |
| Standard Error | Quantitative (continuous) | Measures statistical uncertainty. |
| Type of Days | Qualitative | Categorizes days, such as weekdays or weekends. |
| Age Group | Qualitative (ordinal) | Represents ordered age categories. |
| Activity | Qualitative | Identifies the activity being measured. |
| Sex | Qualitative | Identifies demographic categories. |

### Summary

The dataset contains quantitative measurements of sleeping
duration and statistical uncertainty, along with qualitative
categories describing population groups and reporting periods.

The index column is an identifier rather than an analytical
measurement.


## Dataset 2: Global Trends in Mental Health Disorder

| Column | Classification | Explanation |
|---|---|---|
| index | Identifier | Row number, not a measured quantity. |
| Entity | Qualitative | Identifies a country or region. |
| Code | Qualitative | Country or region identifier. |
| Year | Quantitative (discrete/time) | Represents the year of observation. |
| Schizophrenia (%) | Quantitative (continuous) | Measures schizophrenia prevalence as a percentage. |
| Bipolar disorder (%) | Quantitative (continuous) | Measures bipolar disorder prevalence as a percentage. |
| Eating disorders (%) | Quantitative (continuous) | Measures eating disorder prevalence as a percentage. |
| Anxiety disorders (%) | Quantitative (continuous) | Measures anxiety disorder prevalence as a percentage. |
| Drug use disorders (%) | Quantitative (continuous) | Measures drug use disorder prevalence as a percentage. |
| Depression (%) | Quantitative (continuous) | Measures depression prevalence as a percentage. |
| Alcohol use disorders (%) | Quantitative (continuous) | Measures alcohol use disorder prevalence as a percentage. |

### Summary

The dataset contains qualitative identifiers for countries
and regions, a year variable, and quantitative measurements
of mental health disorder prevalence.

Although some percentage columns are stored as strings or
objects in Pandas, they represent quantitative measurements
and may require cleaning before numerical analysis.


## Dataset 3: Credit Card Approvals

| Column | Classification | Explanation |
|---|---|---|
| Gender | Qualitative (nominal) | Represents gender categories encoded as numbers. |
| Age | Quantitative (continuous) | Measures the applicant's age. |
| Debt | Quantitative (continuous) | Measures the applicant's debt-related value. |
| Married | Qualitative (binary) | Indicates marital status using 0 or 1. |
| BankCustomer | Qualitative (binary) | Indicates whether the applicant is a bank customer. |
| Industry | Qualitative (nominal) | Identifies an industry category. |
| Ethnicity | Qualitative (nominal) | Identifies an ethnicity category. |
| YearsEmployed | Quantitative (continuous) | Measures length of employment. |
| PriorDefault | Qualitative (binary) | Indicates previous default status. |
| Employed | Qualitative (binary) | Indicates employment status. |
| CreditScore | Quantitative (discrete) | Numerical credit-related score. |
| DriversLicense | Qualitative (binary) | Indicates driver's license status. |
| Citizen | Qualitative (nominal) | Identifies citizenship category. |
| ZipCode | Qualitative (nominal) | Postal code used as a location identifier. |
| Income | Quantitative (discrete) | Numerical income value recorded as integers. |
| Approved | Qualitative (binary) | Indicates whether the application was approved. |

### Summary

The Credit Card Approvals dataset contains both quantitative
and qualitative variables.

Quantitative variables include age, debt, years employed,
credit score, and income.

Qualitative variables include gender, marital status,
employment status, citizenship, and approval status.

Some qualitative variables are encoded as integers (0 and 1).
Their numerical storage type does not make them quantitative.

ZipCode is also qualitative because it identifies a location
rather than measuring a numerical quantity.
