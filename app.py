from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/faculty')
def faculty_dashboard():
    return render_template('faculty_dashboard.html')

@app.route('/student')
def student_panel():
    return render_template('student_panel.html')

@app.route('/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/attendance_flow')
def attendance_flow():
    return render_template('attendance_flow.html')

if __name__ == '__main__':
    app.run(debug=True)
