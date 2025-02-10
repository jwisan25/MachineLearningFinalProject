# MachineLearningFinalProject
My final project for our Machine Learning unit in python


Heart Disease Prediction Report

Problem & Dataset

The goal of this project is to predict heart disease based on patient data. The dataset includes age, cholesterol, blood pressure, heart rate, and other health factors. The target variable is output, where 1 means the person has heart disease and 0 means they don’t.

EDA Findings

-Most people have cholesterol levels between 200-300, but some have much higher levels.

-The dataset is fairly balanced, with slightly more people having heart disease than not.

-Some features, like maximum heart rate and oldpeak (ST depression), seem to have a stronger link to heart disease.

Preprocessing Steps

-Normalized numerical features to make sure they are on the same scale.

-One-hot encoded categorical variables so the model can understand them.

-Removed outliers using Z-scores to avoid extreme values affecting the model.

Modeling Approach & Results

-Used Logistic Regression since it's good for binary classification.

-The model had 81% accuracy, meaning it correctly predicts heart disease most of the time.

-Precision (84%) and Recall (82%) show that the model is good at detecting heart disease but still makes some mistakes.



