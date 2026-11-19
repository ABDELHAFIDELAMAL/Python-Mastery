import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

names = np.array(["Ali", "Sara", "Youssef", "Amine", "Salma",
                  "Omar", "Nora", "Adam", "Meryem", "Hamza"])

math_scores = np.array([15, 18, 12, 16, 19, 10, 17, 14, 20, 13])
python_scores = np.array([16, 19, 14, 17, 18, 11, 16, 15, 20, 12])

average = (math_scores + python_scores) / 2

print("===== NUMPY =====")
print("Average scores:", average)
print("Class average:", np.mean(average))
print("Maximum score:", np.max(average))
print("Minimum score:", np.min(average))
print("Standard deviation:", np.std(average))


# 2. PANDAS - Create a DataFrame
df = pd.DataFrame({
    "Name": names,
    "Math": math_scores,
    "Python": python_scores,
    "Average": average
})

df["Result"] = np.where(df["Average"] >= 10, "Passed", "Failed")

print("\n===== PANDAS =====")
print(df)

print("\nStatistics:")
print(df.describe())

print("\nPassed students:")
print(df[df["Result"] == "Passed"])


# 3. MATPLOTLIB - Bar chart
plt.figure(figsize=(10, 5))

plt.bar(df["Name"], df["Average"])

plt.title("Students Average Scores")
plt.xlabel("Students")
plt.ylabel("Average")
plt.ylim(0, 20)
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()


# 4. SEABORN - Statistical visualization
plt.figure(figsize=(10, 5))

sns.barplot(data=df, x="Name", y="Average")

plt.title("Average Scores - Seaborn")
plt.xlabel("Students")
plt.ylabel("Average")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# 5. SEABORN - Correlation heatmap
plt.figure(figsize=(6, 4))

sns.heatmap(
    df[["Math", "Python", "Average"]].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Between Scores")
plt.tight_layout()
plt.show()

print("\n===== ANALYSIS COMPLETED =====")
