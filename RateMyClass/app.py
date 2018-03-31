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
def index_post():
    text = request.form['text']
    
    cur = mysql.connection.cursor()

    # Get courses
    result = cur.execute("SELECT * FROM courses WHERE title LIKE ?", text)

    courses = cur.fetchall()

    if result > 0:
        return render_template('courses.html', courses=courses)
    else:
        msg = 'No Courses Found'
        return render_template('courses.html', msg=msg)
    # Close connection
    cur.close()

@app.route('/courses')
def courses():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get courses
    result = cur.execute("SELECT * FROM courses")

    courses = cur.fetchall()

    if result > 0:
        return render_template('courses.html', courses=courses)
    else:
        msg = 'No Courses Found'
        return render_template('courses.html', msg=msg)
    # Close connection
    cur.close()

@app.route('/course/<string:id>/')
def course(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get course
    result = cur.execute("SELECT * FROM courses WHERE id = %s", [id])

    course = cur.fetchone()

    return render_template('course.html', course=course)

if __name__ == '__main__':
	app.run(debug=True)

