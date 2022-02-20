from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<string:title>')
@app.route('/index/<string:title>')
def index(title):
    params = {
        "title": title
    }
    return render_template('base.html', **params)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
