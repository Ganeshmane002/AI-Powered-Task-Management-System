# AI-Powered Task Management System

## 📌 Project Overview

This project focuses on building an intelligent task management system using Machine Learning and Natural Language Processing (NLP). The system automatically classifies tasks, predicts their priority, and assists in efficient task allocation based on workload and deadlines.

---

## 🎯 Objectives

* Classify tasks into categories using NLP
* Predict task priority based on deadlines and workload
* Enable efficient workload balancing
* Provide an interactive interface using Streamlit

---

## 🛠️ Tech Stack

### Languages & Libraries

* Python
* Pandas, NumPy
* Scikit-learn
* NLTK
* Joblib

### Models Used

* Naive Bayes (Baseline)
* Support Vector Machine (SVM) – Task Classification
* Random Forest – Priority Prediction

### Tools

* Google Colab
* Streamlit (for UI)
* GitHub (Version Control)

---

## 📂 Project Structure

```
AI-Powered-Task-Management-System/
│
├── data/
│   └── task_management_dataset.csv
│
├── models/
│   ├── svm_model.joblib
│   ├── tfidf_vectorizer.joblib
│   └── priority_model.joblib
│
├── notebooks/
│   └── AI-Powered-Task-Management-System.ipynb
│
├── app/
│   └── app.py
│
└── requirements.txt
```

---

## ⚙️ Workflow

### 1. Data Preprocessing

* Lowercasing text
* Removing special characters
* Removing stopwords
* Stemming

### 2. Feature Engineering

* TF-IDF Vectorization (unigrams + bigrams)

### 3. Model Training

* Naive Bayes for baseline performance
* SVM for task classification
* Random Forest for priority prediction

### 4. Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score

## 🚀 How to Run the Project

### Step 1: Install Dependencies

```
pip install -r requirements.txt
```

### Step 2: Run Notebook

* Open `notebooks/AI-Powered-Task-Management-System.ipynb`
* Run all cells to train models

### Step 3: Run Streamlit App

```
streamlit run app.py
```

---

## 🧠 Sample Prediction

**Input:**

* Task: "Create sales dashboard using Power BI"
* Deadline: 5 days
* Effort: 10 hours
* Workload: 40 hours
* Completion Rate: 0.8

**Output:**

* Category: Reporting
* Priority: Medium

---

## 📈 Features

* Automated task classification
* Priority prediction using ML
* Workload-aware task handling
* Interactive UI with Streamlit

---

## 🔮 Future Improvements

* Use BERT for advanced NLP
* Integrate real-time APIs (Jira, Trello)
* Advanced workload balancing using ML
* Deploy on cloud platforms

---

## 👨‍💻 Author

Ganesh Mane

---

## 📌 Conclusion

This project demonstrates how machine learning and NLP can be effectively applied to automate task management processes, improving efficiency, accuracy, and decision-making in real-world scenarios.
