from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    list1 = ["vasim", "ut", 'shaikh', "sofiya"]
    number = ["1", "2", '3', "4"]
    return render_template('index.html',  list1=list1, number=number)


if __name__ == '__main__':
    app.run(debug=True)
