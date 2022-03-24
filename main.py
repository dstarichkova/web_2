from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/<string:title>')
@app.route('/index/<string:title>')
def index(title):
    params = {
        "title": title
    }
    return render_template('base.html', **params)


@app.route('/training/<string:prof>')
def training(prof):
    params = {
        "prof": prof
    }
    return render_template('training.html', **params)


@app.route('/list_prof/<string:list_type>')
def list_prof(list_type):
    with open("profs.json", "rt", encoding="utf8") as f:
        profs_list = json.loads(f.read())
    params = {
        "list_type": list_type,
        "profs_list": profs_list
    }
    return render_template('profs.html', **params)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
