from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    name = "vasim shaikh "
    list1 = list(name)
    dict = {'vasm': "shaikh"}
    return render_template('index.html', name=name, list1=list1, dict=dict)


if __name__ == '__main__':
    app.run(debug=True)
