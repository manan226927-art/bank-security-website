from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# 🔗 MongoDB connection (REPLACE with YOUR connection string)
import os
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection using environment variable
MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client["bank_security_db"]
collection = db["bank_details"]

# 📦 Database & Collection
db = client["bank_security_db"]
collection = db["bank_details"]

# 🏠 Home / Login page
@app.route("/")
def index():
    return render_template("index.html")

# 📊 Dashboard page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# 🤖 AI page (optional)
@app.route("/ai")
def ai():
    return render_template("ai.html")

# 🏦 Bank Form (GET + POST)
@app.route("/bank", methods=["GET", "POST"])
def bank():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "account": request.form["account"],
            "ifsc": request.form["ifsc"]
        }

        # 💾 Save to MongoDB
        collection.insert_one(data)

        return redirect("/dashboard")

    return render_template("bank_form.html")

# ▶️ Run app
if __name__ == "__main__":
    app.run(debug=True)

