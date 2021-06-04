from flask import Flask, request, render_template, request, redirect, url_for
from Script import recommendations
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = "SECRET KEY"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234567890'
app.config['MYSQL_DB'] = 'movi'

mysql = MySQL(app)

#HOMEPAGE
@app.route('/')
def home():
    return render_template('index.html')

#ON Click Submit
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        str = request.form
        try:
            movielist = recommendations(str['movie_name'])
            return render_template('index.html', movies=movielist)
        except:
            return render_template('index.html',
                                   error="Please Enter a Valid Movie Name")

    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM accounts WHERE username = % s AND password = % s', (
                username,
                password,
            ))
        account = cursor.fetchone()
        if account:
            msg = 'Logged in successfully !'
            return render_template('login.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
            return render_template('login.html', msg=msg)
    else:
        return render_template('login.html', msg=msg)

@app.route("/register", methods=["GET", "POST"])
def register():
    msg=""
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute('SELECT * FROM accounts WHERE username = % s',
                       (username, ))
        account = cursor.fetchone()

        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)',
                           (
                               username,
                               email,
                               password,
                           ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg=msg)

@app.route("/about-use")
def about():
    return render_template("about-use.html")

if __name__ == '__main__':
    app.run(debug=True)

#Authors:
##Shubh Gupta 199301305
##Gaurav Kumar 199301159