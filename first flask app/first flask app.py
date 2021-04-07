from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/vasim')
def vasim():
    return 'Hello vasim assssssaa !'


if __name__ == '__main__':
    # jar hamne debug mode on kiya to hamara sab work auto save ho gayenga
    app.run(debug=True)
    # app.run()
