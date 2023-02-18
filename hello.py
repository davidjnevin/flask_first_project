from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.config.from_pyfile("settings.py")


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/greeting/<name>")
def hello(name):
	return render_template("hello.html", t_name=name)

@app.route("/form", methods=["GET", "POST"])
def form():
	"""Use get to get any of the variables"""
	if request.method == "POST":
		first_name = request.values.get("first_name")
		last_name = request.values.get("last_name")
		session["first_name"] = first_name
		return redirect(url_for("registered"))
	return render_template("form.html")

@app.route("/thank_you")
def registered():
	first_name = session.get("first_name")
	return f"Thank you, {first_name}!"
