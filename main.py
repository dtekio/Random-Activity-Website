from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    params = {}
    if request.method == "POST":
        params = {
            "type":request.form.get('Type'),
            "participants":request.form.get('Participants'),
        }
    activity = requests.get('http://www.boredapi.com/api/activity', params=params).json()
    return render_template("index.html", activity=activity)


if __name__ == "__main__":
    app.run(debug=True)
