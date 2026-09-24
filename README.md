# Loan Approval Prediction

A moderate-level B.Tech Machine Learning project using Flask, Logistic Regression and SQLite.

## Features
- Applicant loan prediction
- Logistic Regression model
- Probability/confidence display
- SQLite prediction history
- Responsive Bootstrap frontend
- Home, Predict, Result, History and About pages

## Setup

### 1. Open terminal in this project folder
```bash
cd Loan_Approval_Prediction
```

### 2. Create a virtual environment
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the model
```bash
python train_model.py
```

This creates `loan_model.pkl`.

### 5. Create the database
```bash
python init_db.py
```

This creates `database.db`.

### 6. Run the Flask application
```bash
python app.py
```

Open:
http://127.0.0.1:5000

## Important
The included CSV is a synthetic educational dataset created for this project. It is suitable for demonstrating the complete pipeline. For a stronger academic project, replace it with a properly sourced real loan dataset and document its source, preprocessing, train/test split and evaluation metrics.

The prediction is for educational purposes and should not be used as an actual lending decision.
