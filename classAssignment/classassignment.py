import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
y = np.array([0, 1, 0, 1, 0, 1])
y_pred = np.array([0.30, 0.55, 0.75, 0.80, 0.40, 0.70])

# New thresholds
thresholds = [0.2, 0.4, 0.5, 0.65, 0.75, 0.9]

results = []

for t in thresholds:
    y_hat = (y_pred >= t).astype(int)
    
    TP = np.sum((y == 1) & (y_hat == 1))
    TN = np.sum((y == 0) & (y_hat == 0))
    FP = np.sum((y == 0) & (y_hat == 1))
    FN = np.sum((y == 1) & (y_hat == 0))
    
    TPR = TP / (TP + FN)
    FPR = FP / (FP + TN)
    
    results.append([t, TP, FN, FP, TN, TPR, FPR])

df = pd.DataFrame(results, columns=["Threshold","TP","FN","FP","TN","TPR","FPR"])
print(df)

# Sort for ROC
df = df.sort_values(by="FPR")

# Plot
plt.figure(figsize=(6,6))
plt.plot(df["FPR"], df["TPR"], marker='o', label="ROC Curve")
plt.plot([0,1], [0,1], '--', label="Random Line")

for i in range(len(df)):
    plt.text(df["FPR"].iloc[i], df["TPR"].iloc[i],
             f"T={df['Threshold'].iloc[i]}")

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve (New Thresholds)")
plt.legend()
plt.grid()
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
y = np.array([0, 1, 0, 1, 0, 1])
y_pred = np.array([0.30, 0.55, 0.75, 0.80, 0.40, 0.70])

# New thresholds
thresholds = [0.2, 0.4, 0.5, 0.65, 0.75, 0.9]

results = []

for t in thresholds:
    y_hat = (y_pred >= t).astype(int)
    
    TP = np.sum((y == 1) & (y_hat == 1))
    TN = np.sum((y == 0) & (y_hat == 0))
    FP = np.sum((y == 0) & (y_hat == 1))
    FN = np.sum((y == 1) & (y_hat == 0))
    
    TPR = TP / (TP + FN)
    FPR = FP / (FP + TN)
    
    results.append([t, TP, FN, FP, TN, TPR, FPR])

df = pd.DataFrame(results, columns=["Threshold","TP","FN","FP","TN","TPR","FPR"])
print(df)

# Sort for ROC
df = df.sort_values(by="FPR")

# Plot
plt.figure(figsize=(6,6))
plt.plot(df["FPR"], df["TPR"], marker='o', label="ROC Curve")
plt.plot([0,1], [0,1], '--', label="Random Line")

for i in range(len(df)):
    plt.text(df["FPR"].iloc[i], df["TPR"].iloc[i],
             f"T={df['Threshold'].iloc[i]}")

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve (New Thresholds)")
plt.legend()
plt.grid()
plt.show()
