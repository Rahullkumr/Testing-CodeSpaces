from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    todos = []
    with open("todos.txt", "r") as f:
        for line in f:
            todos.append(line.strip())

    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    with open("todos.txt", "a") as f:
        f.write(title + "\n")

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
