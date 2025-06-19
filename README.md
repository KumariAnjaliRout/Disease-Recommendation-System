# Disease-Recommendation-System


An AI-powered disease prediction system built using Machine Learning and deployed using Streamlit. The app predicts the most likely disease based on user-selected symptoms and provides useful health-related information such as description and precautions.

![Streamlit App Preview](https://img.shields.io/badge/Built%20With-Streamlit-blue) ![Made with Python](https://img.shields.io/badge/Made%20with-Python-green)

---

## Overview

The system uses a trained RandomForestClassifier to predict diseases from symptoms entered by the user. After predicting the disease, it displays:

- A short **description**
- A list of **precautions** to follow

---

##  Live Demo

> Want to try the app? https://disease-recommendation-system-jakkv3kvtcgcnwfrxykedz.streamlit.app/

---

## Features

-  130+ symptoms used for training
-  Predicts from 40+ known diseases
-  User-friendly interface using **Streamlit**
-  Personalized recommendations (description + precautions)
-  Supports multiple symptoms at once
-  Ready for deployment or local testing

---

##  Dataset

- `dataset.csv` – Cleaned dataset with binary-encoded symptoms
- `symptom_Description.csv` – Descriptions for each disease
- `symptom_precaution.csv` – Precautions to take per disease

---

##  Tech Stack

| Technology | Description |
|------------|-------------|
| Python     | Core programming language |
| Pandas / NumPy | Data handling |
| Scikit-learn | Machine learning (Random Forest) |
| Streamlit  | Web application framework |
| Pickle     | Model serialization |

---

