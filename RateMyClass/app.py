from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'ratemyclass'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def courses_post():
    cur = mysql.connection.cursor()

    # Get courses
    cur.execute("SELECT * FROM coursetable WHERE DEPARTMENT LIKE '%s'" % request.form['text'])

    coursetable = cur.fetchall()

    return render_template('courses.html', coursetable=coursetable)
    # Close connection

@app.route('/courses')
def courses():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get courses
    result = cur.execute("SELECT * FROM coursetable")

    coursetable = cur.fetchall()

    if result > 0:
        return render_template('courses.html', coursetable=coursetable)
    else:
        msg = 'No Courses Found'
        return render_template('courses.html', msg=msg)
    # Close connection
    cur.close()

@app.route('/course/<string:SECTION>/')
def course(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get course
    result = cur.execute("SELECT * FROM coursetable WHERE SECTION = %s", [SECTION])

    course = cur.fetchone()

    return render_template('course.html', course=course)

if __name__ == '__main__':
	app.run(debug=True)