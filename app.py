from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/departments')
def departments():
    return render_template('departments.html')

@app.route('/departments/tamil')
def tamil_department():
    return render_template('tamil.html')

@app.route('/departments/tamil/faculty')
def tamil_faculty():
    return render_template('tamil_faculty.html')

@app.route('/departments/tamil/syllabus')
def tamil_syllabus():
    return render_template('tamil_syllabus.html')

@app.route('/departments/tamil/peos')
def tamil_peos():
    return render_template('tamil_peos.html')

@app.route('/departments/tamil/notices')
def tamil_notices():
    return render_template('tamil_notices.html')

@app.route('/departments/english')
def english_department():
    return render_template('english.html')

@app.route('/departments/history')
def history_department():
    return render_template('history.html')

@app.route('/departments/mathematics')
def mathematics_department():
    return render_template('mathematics.html')

@app.route('/departments/Physics')
def physics_department():
    return render_template('physics.html')

@app.route('/departments/Chemistry')
def chemistry_department():
    return render_template('chemistry.html')

@app.route('/departments/Zoology')
def zoology_department():
    return render_template('zoology.html')

@app.route('/departments/Botany')
def botany_department():
    return render_template('botany.html')

@app.route('/departments/Computer Science')
def computer_science_department():
    return render_template('computer_science.html')

@app.route('/departments/Commerce')
def commerce_department():
    return render_template('commerce.html')

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