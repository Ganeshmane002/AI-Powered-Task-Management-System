import streamlit as st
import joblib
import re
import nltk
import pandas as pd

# ------------------ NLTK Setup ------------------
try:
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
except:
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

# ------------------ Load Models ------------------
svm_model = joblib.load("svm_model.joblib")
tfidf = joblib.load("tfidf_vectorizer.joblib")
rf_model = joblib.load("priority_model.joblib")

# Load dataset (for workload balancing)
df = pd.read_csv(r"C:\Users\admin\Downloads\task_management_dataset.csv")

# ------------------ Styling ------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #141E30, #243B55);
    color: white;
}

/* Title */
.title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: #00C9FF;
}

/* Input labels (IMPORTANT FIX) */
label {
    color: white !important;
    font-weight: 500;
}

/* Text area */
textarea {
    background-color: #f0f0f0 !important;
    color: black !important;
}

/* Sliders text */
.stSlider label {
    color: white !important;
}

/* Card */
.card {
    background-color: #1f2c3d;
    padding: 20px;
    border-radius: 12px;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ Functions ------------------

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [stemmer.stem(w) for w in words if w not in stop_words]
    return " ".join(words)

# Workload balancing logic
def assign_employee(task_effort):
    
    emp_df = df.groupby('assigned_employee', as_index=False)['employee_current_workload_hours'].mean()
    
    # Add incoming task effort
    emp_df['updated_workload'] = emp_df['employee_current_workload_hours'] + task_effort
    
    # Select employee with minimum workload
    emp_df = emp_df.sort_values('updated_workload')
    
    return emp_df.iloc[0]['assigned_employee']

# ------------------ UI ------------------

st.markdown('<div class="title">AI-Powered Task Management System</div>', unsafe_allow_html=True)

task_desc = st.text_area("Enter Task Description")
deadline = st.slider("Deadline (days)", 1, 30)
effort = st.slider("Effort (hours)", 1, 40)
workload = st.slider("Employee Workload", 10, 160)
completion = st.slider("Completion Rate", 0.5, 1.0)

# ------------------ Prediction ------------------

predict_clicked = st.button("Predict")

if predict_clicked:
    clean = preprocess(task_desc)
    vector = tfidf.transform([clean])
    
    category = svm_model.predict(vector)[0]
    priority = rf_model.predict([[deadline, effort, workload, completion]])[0]
    employee = assign_employee(effort)

    st.markdown(f"""
    <div class="card">
        <h3>○ Category: {category}</h3>
        <h3>○ Priority: {priority}</h3>
        <h3>○ Assigned Employee: {employee}</h3>
    </div>
    """, unsafe_allow_html=True)