import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Encoded training dataset for a moderate college project.
# 1 = Yes/Male/Graduate/Good credit, 0 = No/Female/Not Graduate/Poor credit.
data = pd.read_csv("loan_data.csv")

X = data.drop("Loan_Status", axis=1)
y = data["Loan_Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=1000, random_state=42))
])

model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy * 100:.2f}%")
print(classification_report(y_test, predictions))

with open("loan_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as loan_model.pkl")
