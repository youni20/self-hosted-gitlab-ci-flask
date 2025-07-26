from flask import Flask, render_template, url_for, jsonify
import json
import random

app = Flask(__name__)

last_index = None
quotes = []
author = []
with open("quotes.json", "r") as file:
    data = json.load(file)
    for item in data:
        quotes.append(item["quote"])
        author.append(item["author"])


@app.route("/")
def home():
    quote, auth = getQuote()
    return(render_template("index.html", quote=quote, auth=auth)) # No need to specify folder as by default it looks inside folder named templates. 

@app.route("/api/quote")
def api_quote():
    quote, auth = getQuote()
    return jsonify({"quote": quote, "auth": auth})


def getQuote():
    global last_index
    if len(quotes) == 0:
        return "No quotes available.", "Unknown"
    
    if len(quotes) == 1:
        num = 0
    else:
        num = random.randint(0, len(quotes)-1)
        while num == last_index:
            num = random.randint(0, len(quotes)-1)

    last_index = num
    return quotes[num], author[num]


if __name__ == "__main__":
    app.run(debug=True, port=8000) # Debug=True, so if any errors it shows on webpage.


#15:30