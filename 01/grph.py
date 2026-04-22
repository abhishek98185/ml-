
import matplotlib.pyplot as plt
import seaborn as sns
# Line plot with multiple lines
hours = [1, 3, 5, 7, 9]
marks_A = [15, 25, 40, 55, 70]
marks_B = [10, 20, 35, 45, 60]
plt.plot(hours, marks_A, label="Student A")
plt.plot(hours, marks_B, label="Student B")
plt.title("Marks vs Hours Studied")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")
plt.legend()
plt.show()
# Change plot style
plt.style.use("classic")
plt.plot(hours, marks_A, label="Student A")
plt.plot(hours, marks_B, label="Student B")
plt.title("Multiple Line Plot with Style")
plt.legend()
plt.show()
# Vertical bar plot
marks = [10, 20, 30, 40, 50]
students = [5, 9, 14, 8, 3]
plt.bar(marks, students)
plt.title("Bar Chart")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
# Horizontal bar chart
plt.barh(marks, students)
plt.title("Horizontal Bar Chart")
plt.xlabel("Number of Students")
plt.ylabel("Marks")
plt.show()
# Bar chart with large variation
values = [1200, 900, 1500, 10, 20, 30]
x = [1, 2, 3, 4, 5, 6]
plt.bar(x, values)
plt.title("Bar Chart with Large Variations")
plt.show()
# Handle large variation using log scale
plt.bar(x, values)
plt.yscale("log")
plt.title("Bar Chart using Log Scale")
plt.show()
# Heatmap using seaborn
data = [[45, 80, 30],
[10, 5, 95],
[60, 100, 20]]
sns.heatmap(data)
plt.title("Heatmap")
plt.show()
# Heatmap with annotations
sns.heatmap(data, annot=True)
plt.title("Annotated Heatmap")
plt.show()