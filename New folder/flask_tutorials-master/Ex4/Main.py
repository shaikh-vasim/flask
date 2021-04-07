from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/friends/<name>')
def friend(name):
    return render_template('friends.html', name=name)
if __name__ == '__main__':
    app.run(debug=True)
