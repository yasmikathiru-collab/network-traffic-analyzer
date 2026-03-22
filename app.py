from flask import Flask, render_template, jsonify, request, redirect, session, send_file
from capture import start_sniffing, captured_data
import threading

# PDF
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)
app.secret_key = "secret123"

# Login credentials
USERNAME = "admin"
PASSWORD = "1234"

# Start packet sniffing in background
def run_sniffer():
    start_sniffing()

# ---------------- LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == USERNAME and request.form["password"] == PASSWORD:
            session["user"] = request.form["username"]
            return redirect("/dashboard")
    return render_template("login.html")

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")
    return render_template("index.html")

# ---------------- DATA API ----------------
@app.route("/data")
def get_data():
    return jsonify(captured_data)

# ---------------- PDF REPORT ----------------
@app.route("/report")
def generate_report():
    if "user" not in session:
        return redirect("/")

    doc = SimpleDocTemplate("report.pdf")
    styles = getSampleStyleSheet()

    content = []

    for packet in captured_data:
        text = str(packet)
        content.append(Paragraph(text, styles["Normal"]))

    doc.build(content)

    return send_file("report.pdf", as_attachment=True)

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    thread = threading.Thread(target=run_sniffer)
    thread.daemon = True
    thread.start()

    app.run(debug=True)