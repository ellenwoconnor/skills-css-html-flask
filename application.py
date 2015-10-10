from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""
    return render_template("index.html")

@app.route("/application")
def apply():
    """Request job application info from user."""
    return render_template("application_form.html")

@app.route("/confirmation", methods=["POST"])
def confirm():
    """Display a personalized confirmation page."""
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = request.form.get("salary")
    job = request.form.get("job")
    return render_template("confirmation.html", firstname=firstname,
        lastname=lastname, salary=salary, job=job)


if __name__ == "__main__":
    app.run(debug=True)
