# -*- coding: utf-8 -*-
"""FinalProject

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bOO1mvix6vb5q6h0suMVSXg36x2q2ock

#Dataset Summary

The dataset contains 302 rows and 14 columns.

It has both numerical and categorical features in it.

The target variable is binary (0 or 1) which shows if the person has heart disease or not.

No missing values are present.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cleaned_heart_data.csv')
df.info()
df.count()

"""The first graph shows that most people have cholesterol levels between 200 and 300, with a few having much higher levels. The second graph shows that slightly more people in the dataset have heart disease than those who don't."""

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.histplot(df["chol"], bins=30, kde=True, color="blue")
plt.xlabel("Cholesterol Level")
plt.ylabel("Frequency")
plt.title("Distribution of Cholesterol Levels")
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(x=df["output"], palette="coolwarm")
plt.xlabel("Heart Disease (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.title("Heart Disease Distribution in the Dataset")
plt.xticks(ticks=[0, 1], labels=["No Disease", "Disease"])
plt.show()

from sklearn.preprocessing import StandardScaler

num_features = ["age", "trtbps", "chol", "thalachh", "oldpeak"]
df[num_features] = StandardScaler().fit_transform(df[num_features])

df = df[(df[num_features].abs() < 3).all(axis=1)]

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

X = df.drop(columns=["output"])
y = df["output"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

metrics = {
    "Accuracy": accuracy_score(y_test, y_pred),
    "Precision": precision_score(y_test, y_pred),
    "Recall": recall_score(y_test, y_pred),
    "F1 Score": f1_score(y_test, y_pred)
}

metrics_df = pd.DataFrame(metrics.items(), columns=["Metric", "Value"])

plt.figure(figsize=(6, 5))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues",
            xticklabels=["No Disease", "Disease"], yticklabels=["No Disease", "Disease"])
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.show()

from sklearn.metrics import classification_report

report = classification_report(y_test, y_pred, output_dict=True)

print(classification_report(y_test, y_pred))

"""Logistic Regression is 81% accurate at predicting heart disease. It's simple, fast, and explains which factors matter, but it struggles with complex patterns. It works well when data is balanced but might fail if one class is much bigger than the other."""