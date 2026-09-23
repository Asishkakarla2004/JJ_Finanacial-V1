from flask import Flask, render_template, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)

CONTACTS = []

LOANS = [
    {"id": 1, "loan_type": "Home Loan", "amount": 4500000, "status": "Completed", "date": "12 Sep 2026", "interest": 7.0},
    {"id": 2, "loan_type": "Personal Loan", "amount": 650000, "status": "Active", "date": "05 Sep 2026", "interest": 11.5},
    {"id": 3, "loan_type": "Education Loan", "amount": 850000, "status": "Active", "date": "28 Aug 2026", "interest": 8.5},
    {"id": 4, "loan_type": "Vehicle Loan", "amount": 1200000, "status": "Completed", "date": "18 Aug 2026", "interest": 9.0},
    {"id": 5, "loan_type": "Business Loan", "amount": 2500000, "status": "Pending", "date": "10 Aug 2026", "interest": 12.0},
    {"id": 6, "loan_type": "Gold Loan", "amount": 300000, "status": "Active", "date": "02 Aug 2026", "interest": 10.0},
    {"id": 7, "loan_type": "Home Loan", "amount": 3200000, "status": "Active", "date": "22 Jul 2026", "interest": 7.25},
    {"id": 8, "loan_type": "Personal Loan", "amount": 400000, "status": "Completed", "date": "14 Jul 2026", "interest": 11.0},
    {"id": 9, "loan_type": "Education Loan", "amount": 950000, "status": "Pending", "date": "03 Jul 2026", "interest": 8.25},
    {"id": 10, "loan_type": "Vehicle Loan", "amount": 900000, "status": "Completed", "date": "28 Jun 2026", "interest": 9.25},
]

LOAN_TYPES = [
    {"name": "Home Loan", "icon": "⌂", "rate": 7.0, "desc": "Flexible financing for your dream home."},
    {"name": "Personal Loan", "icon": "◉", "rate": 11.5, "desc": "Quick funds for personal needs and plans."},
    {"name": "Education Loan", "icon": "▣", "rate": 8.5, "desc": "Support for higher education and career goals."},
    {"name": "Vehicle Loan", "icon": "◆", "rate": 9.0, "desc": "Finance your next car or two-wheeler."},
    {"name": "Business Loan", "icon": "▤", "rate": 12.0, "desc": "Working capital and business expansion funding."},
    {"name": "Gold Loan", "icon": "◇", "rate": 10.0, "desc": "Unlock value from your gold with simple financing."},
]

@app.route("/")
def home():
    return render_template("index.html", loans=LOANS, loan_types=LOAN_TYPES)

@app.route("/history")
def history():
    return render_template("history.html", loans=LOANS)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.post("/api/contact")
def submit_contact():
    data = request.get_json(silent=True) or request.form
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    phone = (data.get("phone") or "").strip()
    message = (data.get("message") or "").strip()

    if not name or not email or not message:
        return jsonify({"ok": False, "message": "Name, email and message are required."}), 400

    CONTACTS.append({
        "id": random.randint(1000, 9999),
        "name": name,
        "email": email,
        "phone": phone,
        "message": message,
        "created_at": datetime.now().strftime("%d %b %Y, %I:%M %p")
    })
    return jsonify({"ok": True, "message": "Thanks! Your request has been submitted. Our team will contact you shortly."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
