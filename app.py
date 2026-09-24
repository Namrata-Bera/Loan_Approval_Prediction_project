from flask import Flask, render_template, request
import sqlite3
import pickle
import numpy as np

app = Flask(__name__)
MODEL_PATH = "loan_model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("predict.html")

    try:
        gender = 1 if request.form["gender"] == "Male" else 0
        married = 1 if request.form["married"] == "Yes" else 0
        dependents = request.form["dependents"]
        dependents = 3 if dependents == "3+" else int(dependents)
        education = 0 if request.form["education"] == "Graduate" else 1
        self_employed = 1 if request.form["self_employed"] == "Yes" else 0
        applicant_income = float(request.form["applicant_income"])
        coapplicant_income = float(request.form["coapplicant_income"])
        loan_amount = float(request.form["loan_amount"])
        loan_term = float(request.form["loan_term"])
        credit_history = float(request.form["credit_history"])
        property_area = {"Urban": 2, "Semiurban": 1, "Rural": 0}[request.form["property_area"]]

        features = np.array([[
            gender, married, dependents, education, self_employed,
            applicant_income, coapplicant_income, loan_amount,
            loan_term, credit_history, property_area
        ]])

        prediction = int(model.predict(features)[0])
        probability = float(model.predict_proba(features)[0][prediction] * 100)

        status = "Approved" if prediction == 1 else "Rejected"

        conn = get_db()
        conn.execute("""
            INSERT INTO predictions
            (gender, married, dependents, education, self_employed,
             applicant_income, coapplicant_income, loan_amount,
             loan_term, credit_history, property_area, result, probability)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (gender, married, dependents, education, self_employed,
              applicant_income, coapplicant_income, loan_amount,
              loan_term, credit_history, property_area, status, probability))
        conn.commit()
        conn.close()

        return render_template("result.html", status=status, probability=round(probability, 2))

    except (ValueError, KeyError):
        return render_template("result.html",
                               status="Invalid Input",
                               probability=0,
                               error="Please enter valid values in all fields."), 400

@app.route("/history")
def history():
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM predictions ORDER BY id DESC LIMIT 20"
    ).fetchall()
    conn.close()
    return render_template("history.html", rows=rows)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
