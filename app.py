from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/peixes")
def peixes():
    return render_template("peixes.html")

if __name__ == "__main__":
    app.run(debug=True)