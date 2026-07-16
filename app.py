from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/departments')
def departments():
    return render_template('departments.html')

@app.route('/faculty')
def faculty():
    return render_template('faculty.html')
    
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
    app.run(debug=True)