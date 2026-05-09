# Student Performance Prediction System

The Student Performance Prediction System is a Machine Learning-based web application that predicts student academic performance using factors such as study time, previous failures, absences, internet access, family support, school support, and extracurricular activities.

The project uses multiple Machine Learning algorithms including Logistic Regression, Decision Tree, Random Forest, Support Vector Machine (SVM), and Naive Bayes. Random Forest was selected as the best-performing model.

---

# Features

- Student performance prediction
- Grade classification (A, B, C, F)
- Multiple ML model comparison
- Data preprocessing and feature engineering
- Exploratory Data Analysis (EDA)
- Confusion matrix and evaluation metrics
- Train-test dataset saving
- Model saving/loading using Joblib
- Interactive Streamlit frontend
- Dataset analytics and visualizations

---

# Technologies Used

## Programming Language
- Python

## Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

# Dataset Used

UCI Student Performance Dataset (`student-mat.csv`)

Dataset Source:  
https://archive.ics.uci.edu/dataset/320/student+performance

---

# Machine Learning Algorithms Used

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- Naive Bayes

Random Forest was selected as the final model because it provided the best accuracy.

---

# Project Structure

```text
Student-Performance-Prediction-System/
│
├── student-mat.csv
├── student_performance_prediction.ipynb
├── app.py
├── model.pkl
├── label_encoder.pkl
├── train_data.csv
├── test_data.csv
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/Student-Performance-Prediction-System.git
```

## Open Project Folder

```bash
cd Student-Performance-Prediction-System
```

## Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# Run the Project

## Run Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
student_performance_prediction.ipynb
```

Run all cells to:
- preprocess data
- train models
- evaluate performance
- save trained model

---

## Run Streamlit Frontend

```bash
streamlit run app.py
```

The application will open in the browser at:

```text
http://localhost:8501
```

---

# Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

# Frontend Features

- Student data input form
- Real-time performance prediction
- Risk analysis
- Interactive analytics dashboard
- Graph visualizations

---

# Future Enhancements

- Database integration
- Real-time monitoring
- AI-based recommendation system
- Mobile application
- Teacher dashboard
- Cloud deployment

---

# Conclusion

This project demonstrates how Machine Learning can be used in educational systems to predict student performance and support data-driven academic decisions.

---

# Author

Praneeta Narayan Yaji
