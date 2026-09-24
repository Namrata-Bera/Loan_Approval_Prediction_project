import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gender INTEGER NOT NULL,
    married INTEGER NOT NULL,
    dependents INTEGER NOT NULL,
    education INTEGER NOT NULL,
    self_employed INTEGER NOT NULL,
    applicant_income REAL NOT NULL,
    coapplicant_income REAL NOT NULL,
    loan_amount REAL NOT NULL,
    loan_term REAL NOT NULL,
    credit_history REAL NOT NULL,
    property_area INTEGER NOT NULL,
    result TEXT NOT NULL,
    probability REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()
print("database.db created successfully.")
