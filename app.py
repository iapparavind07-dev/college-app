from flask import Flask, render_template
from departments_data import departments

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/departments')
def departments_page():
    return render_template('departments.html')

@app.route('/departments/<dept_id>')
def department_page(dept_id):
    dept = departments.get(dept_id)
    if dept is None:
        return "Department not found", 404
    return render_template('department.html', dept=dept, dept_id=dept_id)

@app.route('/departments/<dept_id>/<section>')
def department_section(dept_id, section):
    dept = departments.get(dept_id)
    if dept is None:
        return "Department not found", 404
    return render_template('department_section.html', dept=dept, dept_id=dept_id, section=section)

@app.route('/notices')
def notices():
    return render_template('notices.html')

@app.route('/timetable')
def timetable():
    return render_template('timetable.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)