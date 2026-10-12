# 🏦 Loan Approval Prediction

A machine learning-based web application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on applicant and financial information.

The project combines a **Python Flask backend**, **Machine Learning**, **SQLite database**, and a responsive **HTML/CSS/JavaScript frontend**.

---

## 📌 Project Overview

Loan approval decisions depend on several factors such as income, loan amount, credit history, and property information.

This project uses a trained machine learning model to analyze applicant information and provide a predicted loan status through an easy-to-use web interface.

---

## ✨ Features

- 🔐 Applicant information input
- 🤖 Machine learning-based loan prediction
- 📊 Prediction confidence display
- 📝 Prediction history
- 💾 SQLite database integration
- 🌐 Flask web application
- 📱 Responsive and user-friendly interface
- 📈 Approved / Rejected result visualization
- 📖 About page explaining the project

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap / Custom CSS

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Database
- SQLite

### Development Tools
- Visual Studio Code
- Git
- GitHub

---

## 🧠 Machine Learning

The application uses a supervised machine learning classification model to predict loan approval status.

### Input Features

The model considers applicant-related information such as:

- Applicant income
- Co-applicant income
- Loan amount
- Loan term
- Credit history
- Property area
- Other applicant information

### Output

The model predicts:

```text
Approved

or

Rejected
---

## 📂 Project Structure

```text
Loan_Approval_Prediction/
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates/
│   ├── about.html
│   ├── base.html
│   ├── history.html
│   ├── index.html
│   ├── predict.html
│   └── result.html
│
├── app.py
├── init_db.py
├── loan_data.csv
├── loan_model.pkl
├── requirements.txt
├── train_model.py
├── README.md
└── .gitignore
---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Loan_Approval_Prediction.git