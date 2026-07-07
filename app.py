"""
app.py
------
Flask backend. This is the "brain" that:
  1. Serves HTML pages (frontend) to the browser
  2. Receives form data from the user
  3. Calls calculator.py to do the math
  4. Calls database.py to save/fetch data
  5. Sends the result back to be displayed
"""

from flask import Flask, render_template, request, redirect, url_for

import calculator
import database

app = Flask(__name__)


@app.route("/")
def index():
    """Show the input form."""
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    """Receive form data, calculate results, save to DB, show result page."""
    name = request.form.get("name")
    age = int(request.form.get("age"))

    subjects = request.form.getlist("subject_name[]")
    marks = [int(m) for m in request.form.getlist("subject_marks[]")]

    total_marks = sum(marks)
    percentage = calculator.calculate_percentage(marks)
    grade = calculator.calculate_grade(percentage)
    result = calculator.calculate_result(percentage)
    highest, lowest = calculator.highest_lowest(subjects, marks)

    student_id = database.add_student(
        name, age, subjects, marks, total_marks, percentage, grade, result
    )

    return render_template(
        "result.html",
        name=name,
        age=age,
        subjects=zip(subjects, marks),
        total_marks=total_marks,
        percentage=percentage,
        grade=grade,
        result=result,
        highest=highest,
        lowest=lowest,
        student_id=student_id,
    )


@app.route("/history")
def history():
    """Show all previously calculated students."""
    students = database.get_all_students()
    return render_template("history.html", students=students)


@app.route("/delete/<int:student_id>", methods=["POST"])
def delete(student_id):
    """Delete a student record."""
    database.delete_student(student_id)
    return redirect(url_for("history"))


if __name__ == "__main__":
    database.init_db()
    app.run(debug=True)
