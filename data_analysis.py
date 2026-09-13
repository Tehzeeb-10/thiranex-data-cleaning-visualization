# ============================================================
# THIRANEX - DATA CLEANING & VISUALIZATION PROJECT
# ============================================================

# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 2. LOAD DATASET
# ============================================================

file_path = r"D:\anaconda\Book1.xlsx"

df = pd.read_excel(file_path)

print("================================================")
print("DATA CLEANING & VISUALIZATION PROJECT")
print("================================================")

print("\nOriginal Dataset Shape:", df.shape)


# ============================================================
# 3. UNDERSTANDING THE DATASET
# ============================================================

print("\n------------------------------------------------")
print("FIRST 5 ROWS")
print("------------------------------------------------")

print(df.head())


print("\n------------------------------------------------")
print("COLUMN NAMES")
print("------------------------------------------------")

print(df.columns.tolist())


print("\n------------------------------------------------")
print("DATA TYPES")
print("------------------------------------------------")

print(df.dtypes)


print("\n------------------------------------------------")
print("DATASET INFORMATION")
print("------------------------------------------------")

print(df.info())


# ============================================================
# 4. CHECK MISSING VALUES
# ============================================================

print("\n------------------------------------------------")
print("MISSING VALUES BEFORE CLEANING")
print("------------------------------------------------")

print(df.isnull().sum())


# ============================================================
# 5. CHECK DUPLICATE ROWS
# ============================================================

print("\n------------------------------------------------")
print("DUPLICATE ROWS BEFORE CLEANING")
print("------------------------------------------------")

print("Duplicate Rows:", df.duplicated().sum())


# ============================================================
# 6. CHECK DUPLICATE CUSTOMER IDs
# ============================================================

print("\n------------------------------------------------")
print("DUPLICATE CUSTOMER IDs")
print("------------------------------------------------")

duplicate_ids = df[df["CustomerID"].duplicated(keep=False)]

print(duplicate_ids.sort_values("CustomerID"))


# ============================================================
# 7. DATA CLEANING
# ============================================================

# Remove exact duplicate rows
df = df.drop_duplicates()

# Fill missing Profession values
df["Profession"] = df["Profession"].fillna(
    df["Profession"].mode()[0]
)

# Fill missing Season values
df["Season"] = df["Season"].fillna(
    df["Season"].mode()[0]
)


# ============================================================
# 8. CHECK DATA AFTER CLEANING
# ============================================================

print("\n------------------------------------------------")
print("DATA AFTER CLEANING")
print("------------------------------------------------")

print("Cleaned Dataset Shape:", df.shape)


print("\nMissing Values After Cleaning:")

print(df.isnull().sum())


print("\nDuplicate Rows After Cleaning:")

print(df.duplicated().sum())


# ============================================================
# 9. STATISTICAL ANALYSIS
# ============================================================

print("\n------------------------------------------------")
print("AGE STATISTICS")
print("------------------------------------------------")

print(df["Age"].describe())


print("\n------------------------------------------------")
print("PURCHASE AMOUNT STATISTICS")
print("------------------------------------------------")

print(df["Purchase Amount"].describe())


# ============================================================
# 10. AGE OUTLIER DETECTION USING IQR
# ============================================================

Q1_age = df["Age"].quantile(0.25)
Q3_age = df["Age"].quantile(0.75)

IQR_age = Q3_age - Q1_age

lower_age = Q1_age - 1.5 * IQR_age
upper_age = Q3_age + 1.5 * IQR_age

age_outliers = df[
    (df["Age"] < lower_age) |
    (df["Age"] > upper_age)
]

print("\n------------------------------------------------")
print("AGE OUTLIER ANALYSIS")
print("------------------------------------------------")

print("Q1:", Q1_age)
print("Q3:", Q3_age)
print("IQR:", IQR_age)
print("Lower Limit:", lower_age)
print("Upper Limit:", upper_age)
print("Number of Statistical Outliers:", len(age_outliers))

print("\nNote: Age values were retained because they")
print("represent valid customer ages.")


# ============================================================
# 11. PURCHASE AMOUNT OUTLIER DETECTION USING IQR
# ============================================================

Q1_amount = df["Purchase Amount"].quantile(0.25)
Q3_amount = df["Purchase Amount"].quantile(0.75)

IQR_amount = Q3_amount - Q1_amount

lower_amount = Q1_amount - 1.5 * IQR_amount
upper_amount = Q3_amount + 1.5 * IQR_amount

amount_outliers = df[
    (df["Purchase Amount"] < lower_amount) |
    (df["Purchase Amount"] > upper_amount)
]

print("\n------------------------------------------------")
print("PURCHASE AMOUNT OUTLIER ANALYSIS")
print("------------------------------------------------")

print("Q1:", Q1_amount)
print("Q3:", Q3_amount)
print("IQR:", IQR_amount)
print("Lower Limit:", lower_amount)
print("Upper Limit:", upper_amount)
print("Number of Outliers:", len(amount_outliers))


# ============================================================
# 12. CATEGORY COUNTS
# ============================================================

category_count = df["Category"].value_counts()

print("\n------------------------------------------------")
print("CATEGORY-WISE PURCHASES")
print("------------------------------------------------")

print(category_count)


# ============================================================
# 13. GENDER COUNTS
# ============================================================

gender_count = df["Gender"].value_counts()

print("\n------------------------------------------------")
print("GENDER DISTRIBUTION")
print("------------------------------------------------")

print(gender_count)


# ============================================================
# 14. SUBSCRIPTION STATUS
# ============================================================

subscription_count = df["Subscription Status"].value_counts()

print("\n------------------------------------------------")
print("SUBSCRIPTION STATUS")
print("------------------------------------------------")

print(subscription_count)


# ============================================================
# 15. SEASON-WISE PURCHASES
# ============================================================

season_count = df["Season"].value_counts()

print("\n------------------------------------------------")
print("SEASON-WISE PURCHASES")
print("------------------------------------------------")

print(season_count)


# ============================================================
# 16. COUNTRY-WISE CUSTOMERS
# ============================================================

country_count = df["Country"].value_counts()

print("\n------------------------------------------------")
print("TOP 10 COUNTRIES")
print("------------------------------------------------")

print(country_count.head(10))


# ============================================================
# 17. ALL VISUALIZATIONS IN ONE FIGURE
# ============================================================

fig, axes = plt.subplots(3, 2, figsize=(12, 14))


# ------------------------------------------------------------
# Graph 1 - Gender
# ------------------------------------------------------------

gender_count.plot(
    kind="bar",
    ax=axes[0, 0]
)

axes[0, 0].set_title("Customers by Gender")
axes[0, 0].set_xlabel("Gender")
axes[0, 0].set_ylabel("Number of Customers")
axes[0, 0].tick_params(axis="x", rotation=0)


# ------------------------------------------------------------
# Graph 2 - Category
# ------------------------------------------------------------

category_count.plot(
    kind="bar",
    ax=axes[0, 1]
)

axes[0, 1].set_title("Number of Purchases by Category")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Number of Purchases")
axes[0, 1].tick_params(axis="x", rotation=45)


# ------------------------------------------------------------
# Graph 3 - Purchase Amount
# ------------------------------------------------------------

axes[1, 0].hist(
    df["Purchase Amount"],
    bins=10
)

axes[1, 0].set_title("Distribution of Purchase Amount")
axes[1, 0].set_xlabel("Purchase Amount")
axes[1, 0].set_ylabel("Number of Customers")


# ------------------------------------------------------------
# Graph 4 - Subscription Status
# ------------------------------------------------------------

subscription_count.plot(
    kind="bar",
    ax=axes[1, 1]
)

axes[1, 1].set_title("Customers by Subscription Status")
axes[1, 1].set_xlabel("Subscription Status")
axes[1, 1].set_ylabel("Number of Customers")
axes[1, 1].tick_params(axis="x", rotation=0)


# ------------------------------------------------------------
# Graph 5 - Season
# ------------------------------------------------------------

season_count.plot(
    kind="bar",
    ax=axes[2, 0]
)

axes[2, 0].set_title("Number of Purchases by Season")
axes[2, 0].set_xlabel("Season")
axes[2, 0].set_ylabel("Number of Purchases")
axes[2, 0].tick_params(axis="x", rotation=0)


# ------------------------------------------------------------
# Graph 6 - Top 10 Countries
# ------------------------------------------------------------

country_count.head(10).plot(
    kind="bar",
    ax=axes[2, 1]
)

axes[2, 1].set_title("Top 10 Countries by Number of Customers")
axes[2, 1].set_xlabel("Country")
axes[2, 1].set_ylabel("Number of Customers")
axes[2, 1].tick_params(axis="x", rotation=45)


# ============================================================
# 18. FINAL GRAPH LAYOUT
# ============================================================

plt.tight_layout()

plt.show()


# ============================================================
# 19. FINAL INSIGHTS
# ============================================================

print("\n================================================")
print("KEY INSIGHTS")
print("================================================")

print("\n1. Dataset:")
print("The dataset contains", len(df), "records after cleaning.")

print("\n2. Gender:")
print("The dataset contains", len(gender_count),
      "gender categories.")

print("Most common gender:",
      gender_count.idxmax())

print("\n3. Product Category:")
print("Most purchased category:",
      category_count.idxmax())

print("\n4. Subscription:")
print("Most common subscription status:",
      subscription_count.idxmax())

print("\n5. Season:")
print("Season with the highest number of purchases:",
      season_count.idxmax())

print("\n6. Country:")
print("Country with the highest number of customers:",
      country_count.idxmax())

print("\n7. Purchase Amount:")
print("Average purchase amount:",
      round(df["Purchase Amount"].mean(), 2))

print("\n8. Age:")
print("Average customer age:",
      round(df["Age"].mean(), 2))


# ============================================================
# 20. SAVE CLEANED DATASET
# ============================================================

output_file = r"D:\thiranex1\cleaned_dataset.xlsx"

df.to_excel(output_file, index=False)

print("\n------------------------------------------------")
print("CLEANED DATASET SAVED")
print("------------------------------------------------")

print("File saved at:")
print(output_file)


# ============================================================
# PROJECT COMPLETED
# ============================================================

print("\n================================================")
print("PROJECT COMPLETED SUCCESSFULLY")
print("================================================")
