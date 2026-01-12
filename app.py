#from flask import Flask, render_template, request
from flask import Flask, render_template, request, redirect


app = Flask(__name__)

notes = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/note", methods=["GET", "POST"])
def note():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            notes.append(task)
    return render_template("note.html", notes=notes)

@app.route("/delete/<int:index>")
def delete(index):
    if index < len(notes):
        notes.pop(index)
    return redirect("/note")


app.run(debug=True)
