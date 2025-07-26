from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home() -> render_template:
    return(render_template("index.html")) # No need to specify folder as by default it looks inside folder named templates. 

if __name__ == "__main__":
    app.run(debug=True, port=8000) # So if any errors it shows on webpage.