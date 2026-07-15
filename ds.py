from pathlib import Path
import sys

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler


SAMPLE_CSV = "customer_sample.csv"
TRANSFORMED_CSV = "transformed_customer_data.csv"


def create_sample_csv(path):
    sample_data = {
        "customer_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        "name": [
            "Anu",
            "Bala",
            "Charan",
            "Divya",
            "Esha",
            "Farhan",
            "Geetha",
            "Hari",
            "Isha",
            "Jagan",
        ],
        "age": [12, 25, 67, 34, 8, 45, 72, 29, 16, 54],
        "gender": ["F", "M", "M", "F", "F", "M", "F", "M", "F", "M"],
        "city": [
            "Chennai",
            "Bengaluru",
            "Chennai",
            "Mumbai",
            "Delhi",
            "Delhi",
            "Mumbai",
            "Chennai",
            "Bengaluru",
            "Mumbai",
        ],
        "annual_income": [0, 520000, 380000, 710000, 0, 850000, 300000, 640000, 0, 920000],
        "spending_score": [25, 61, 35, 82, 18, 77, 29, 69, 31, 88],
    }
    pd.DataFrame(sample_data).to_csv(path, index=False)


def get_age_group(age):
    if age < 18:
        return "child"
    if age < 60:
        return "adult"
    return "senior"


def explain_plots():
    print("\nPlot explanation:")
    print("1. Histogram: Shows the distribution of numerical features.")
    print("   Tall bars show common value ranges. Skewed bars show uneven distribution.")
    print("2. Box plot: Shows median, quartiles, and possible outliers.")
    print("   Points outside the whiskers are possible outliers that may need checking.")


def main():
    csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(SAMPLE_CSV)

    if not csv_path.exists():
        if csv_path.name == SAMPLE_CSV:
            create_sample_csv(csv_path)
            print(f"No CSV path given. Created sample file: {csv_path}")
        else:
            print(f"CSV file not found: {csv_path}")
            return

    df = pd.read_csv(csv_path)

    print("\nFirst 10 rows:")
    print(df.head(10))

    rows, columns = df.shape
    print(f"\nNumber of rows: {rows}")
    print(f"Number of columns: {columns}")

    print("\nSummary statistics for numerical columns:")
    print(df.describe())

    numerical_columns = df.select_dtypes(include="number").columns

    if len(numerical_columns) > 0:
        sns.set_theme(style="whitegrid")

        df[numerical_columns].hist(figsize=(12, 8), bins=10, edgecolor="black")
        plt.suptitle("Histogram of Numerical Features")
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(12, 6))
        sns.boxplot(data=df[numerical_columns])
        plt.title("Box Plot to Detect Outliers")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("\nNo numerical columns found for plotting.")

    explain_plots()

    transformed_df = df.copy()

    if "age" in transformed_df.columns:
        transformed_df["age_group"] = transformed_df["age"].apply(get_age_group)
    else:
        print("\nAge column not found. Skipping age_group feature creation.")

    categorical_columns = transformed_df.select_dtypes(include=["object", "category"]).columns
    transformed_df = pd.get_dummies(transformed_df, columns=categorical_columns, drop_first=False)

    numerical_columns = transformed_df.select_dtypes(include="number").columns
    if len(numerical_columns) > 0:
        scaler = MinMaxScaler()
        transformed_df[numerical_columns] = scaler.fit_transform(transformed_df[numerical_columns])

    transformed_df.to_csv(TRANSFORMED_CSV, index=False)
    print(f"\nTransformed data saved to: {TRANSFORMED_CSV}")


if __name__ == "__main__":
    main()
