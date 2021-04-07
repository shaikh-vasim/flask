import json
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql
from flask_mail import Mail

pymysql.install_as_MySQLdb()


with open('Config.json', 'r') as caa:
    params = json.load(caa)["params"]
    print(params)

local_server = True
app = Flask(__name__)

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)
mail = Mail(app)


if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


class Contact(db.Model):
    # """
    # name,email,phone_num,msg,date
    # """
    srno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12),  nullable=True)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():

    if (request.method == "POST"):
        """ add entry to data base"""

        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contact(name=name, phone_num=phone, msg=message,
                        date=datetime.now(), email=email)

        db.session.add(entry)
        db.session.commit()

        # mail.send_message('New message from ' + name,
        #                   sender=email,
        #                   recipients=[params['gmail-user']],
        #                   body=message + "\n" + phone
        #                   )

    return render_template('contact.html')


class Posts(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(12), nullable=True)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    return render_template('post.html', params=params)


if __name__ == '__main__':
    app.run(debug=True)
