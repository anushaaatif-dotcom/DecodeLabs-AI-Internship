# ==========================================
# AI Project 2 - Data Classification Using AI
# Dataset: Iris Dataset
# Algorithm: Decision Tree Classifier
# ==========================================

# Import Libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("dataset/iris.csv")

print("=" * 50)
print("First 5 Rows")
print("=" * 50)
print(df.head())

# ==========================================
# Dataset Information
# ==========================================

print("\n" + "=" * 50)
print("Dataset Shape")
print("=" * 50)
print(df.shape)

print("\n" + "=" * 50)
print("Dataset Information")
print("=" * 50)
print(df.info())

print("\n" + "=" * 50)
print("Statistical Summary")
print("=" * 50)
print(df.describe())

print("\n" + "=" * 50)
print("Column Names")
print("=" * 50)
print(df.columns)

print("\n" + "=" * 50)
print("Species Count")
print("=" * 50)
print(df["Species"].value_counts())

# ==========================================
# Features and Target
# ==========================================

# Remove Id and Species columns
X = df.drop(["Id", "Species"], axis=1)

# Target Column
y = df["Species"]

# ==========================================
# Split Dataset
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ==========================================
# Train Model
# ==========================================

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

# ==========================================
# Prediction
# ==========================================

prediction = model.predict(X_test)

# ==========================================
# Accuracy
# ==========================================

accuracy = accuracy_score(y_test, prediction)

print("\n" + "=" * 50)
print("Model Accuracy")
print("=" * 50)
print(f"Accuracy : {accuracy * 100:.2f}%")

# ==========================================
# Classification Report
# ==========================================

print("\n" + "=" * 50)
print("Classification Report")
print("=" * 50)
print(classification_report(y_test, prediction))

# ==========================================
# Confusion Matrix
# ==========================================

cm = confusion_matrix(y_test, prediction)

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=model.classes_,
    yticklabels=model.classes_
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.tight_layout()
plt.show()

# ==========================================
# Predict a New Flower
# ==========================================

sample = [[5.1, 3.5, 1.4, 0.2]]

result = model.predict(sample)

print("\n" + "=" * 50)
print("Prediction for New Sample")
print("=" * 50)
print("Input :", sample)
print("Predicted Species :", result[0])

# ==========================================
# Program Finished
# ==========================================

print("\nProject Completed Successfully!")