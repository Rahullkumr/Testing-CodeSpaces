from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
    
@app.route("/namaste")
def hello_world():
    return "Namaste, Duniya!"

if __name__ == "__main__":
    app.run(debug=True)
