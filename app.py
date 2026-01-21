from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/bank-form")
def bank_form():
    return render_template("bank_form.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/ai")
def ai():
    return render_template("ai.html")
    @app.route("/bank", methods=["GET", "POST"])
def bank():
    if request.method == "POST":
        name = request.form["name"]
        account = request.form["account"]
        ifsc = request.form["ifsc"]

        print(name, account, ifsc)  # later we store in MongoDB

        return redirect("/dashboard")

    return render_template("bank_form.html")


if __name__ == "__main__":

    app.run(debug=True)

