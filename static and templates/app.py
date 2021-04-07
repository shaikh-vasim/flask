from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def vasim():
    # return render_template('index.html')
    return "vasim shaikh"


@app.route('/home')
def home():
    name = "vasim how are you"
    return render_template('index.html', name11=name)


if __name__ == '__main__':
    app.run(debug=True)
