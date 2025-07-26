from flask import Flask

app = Flask(__name__)

@app.route("/")
def home() -> str:
    return("Hello")

if __name__ == "__main__":
    app.run(debug=True) # So if any errors it shows on webpage.