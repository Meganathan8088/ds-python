# =====================================
# Step 1 - Import Libraries
# =====================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (8,4)

print("Libraries loaded successfully!")

# =====================================
# Step 2 - Create Sample Dataset
# =====================================

data = {
    "Name": ["Arjun","Rahul","Sneha","Priya","Kiran","Amit","Ravi","Neha","Sita","Anil"],
    "Age": [20,21,19,22,20,23,21,20,22,24],
    "Marks": [85,78,90,88,76,92,81,84,89,95],
    "Height": [170,168,160,165,172,175,169,162,164,178]
}

df = pd.DataFrame(data)

# =====================================
# Step 3 - Display Data
# =====================================

print("\nFirst 10 Rows:")
print(df.head(10))

print("\nNumber of Rows and Columns:")
print(df.shape)

print("\nSummary Statistics:")
print(df.describe())

# =====================================
# Step 4 - Histogram
# =====================================

plt.figure(figsize=(8,4))
sns.histplot(df["Marks"], bins=5, kde=True)
plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# =====================================
# Step 5 - Box Plot
# =====================================

plt.figure(figsize=(8,4))
sns.boxplot(x=df["Marks"])
plt.title("Box Plot of Marks")
plt.show()

# =====================================
# Step 6 - Explanation
# =====================================

print("\nExplanation:")
print("1. Histogram shows how marks are distributed among students.")
print("2. Higher bars indicate more students in that marks range.")
print("3. Box plot helps identify outliers.")
print("4. If there are points outside the box, they are considered outliers.")
