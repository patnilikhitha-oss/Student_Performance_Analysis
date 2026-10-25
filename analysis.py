
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load the dataset
file_path = Path(__file__).parent / "Student_Performance_Analysis_Dataset.csv"
df = pd.read_csv(file_path)

print("STUDENT PERFORMANCE ANALYSIS")
print("-" * 35)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nStatistical summary:")
print(df.describe())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Hypothesis 1: More study hours are associated with higher exam scores
correlation = df["Study_Hours_Per_Day"].corr(
    df["Exam_Score_Out_of_100"]
)
print("\nStudy hours vs exam score correlation:", round(correlation, 3))

# Hypothesis 2: Better attendance is associated with higher exam scores
attendance_corr = df["Attendance_Percent"].corr(
    df["Exam_Score_Out_of_100"]
)
print("Attendance vs exam score correlation:", round(attendance_corr, 3))

# Investigate a possible pattern: more sleep means higher scores
sleep_corr = df["Sleep_Hours_Per_Day"].corr(
    df["Exam_Score_Out_of_100"]
)
print("Sleep hours vs exam score correlation:", round(sleep_corr, 3))

# Chart 1: Study hours and exam scores
plt.figure(figsize=(8, 5))
plt.scatter(
    df["Study_Hours_Per_Day"],
    df["Exam_Score_Out_of_100"]
)
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours Per Day")
plt.ylabel("Exam Score (out of 100)")
plt.tight_layout()
plt.savefig("study_hours_vs_scores.png")
plt.show()

# Chart 2: Attendance and exam scores
plt.figure(figsize=(8, 5))
plt.scatter(
    df["Attendance_Percent"],
    df["Exam_Score_Out_of_100"]
)
plt.title("Attendance vs Exam Scores")
plt.xlabel("Attendance (%)")
plt.ylabel("Exam Score (out of 100)")
plt.tight_layout()
plt.savefig("attendance_vs_scores.png")
plt.show()

# Chart 3: Sleep hours and exam scores
plt.figure(figsize=(8, 5))
plt.scatter(
    df["Sleep_Hours_Per_Day"],
    df["Exam_Score_Out_of_100"]
)
plt.title("Sleep Hours vs Exam Scores")
plt.xlabel("Sleep Hours Per Day")
plt.ylabel("Exam Score (out of 100)")
plt.tight_layout()
plt.savefig("sleep_hours_vs_scores.png")
plt.show()

# Save a plain-language summary
summary = f"""
STUDENT PERFORMANCE ANALYSIS SUMMARY

Dataset: Synthetic student data created for practice.
Number of students: {len(df)}

Study hours and exam score correlation: {correlation:.3f}
Attendance and exam score correlation: {attendance_corr:.3f}
Sleep hours and exam score correlation: {sleep_corr:.3f}

Interpretation:
Correlation values closer to +1 indicate a stronger positive
relationship. Values closer to -1 indicate a stronger negative
relationship. Values near 0 indicate a weaker linear relationship.

These are practice-data results, not conclusions about all students.
Correlation does not prove causation.
"""

Path("analysis_summary.txt").write_text(summary, encoding="utf-8")
print("\nAnalysis complete. Charts and summary have been saved.")
