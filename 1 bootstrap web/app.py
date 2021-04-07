from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def vasim():
    return render_template("index.html")


@app.route('/aaa')
def vasimaa():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
