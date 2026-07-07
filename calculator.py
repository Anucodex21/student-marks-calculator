"""
calculator.py
-------------
Pure calculation logic. No Flask, no database — just functions that
take numbers in and give numbers/labels out. Kept separate so the
same logic can be tested or reused anywhere (web, CLI, API).
"""


def calculate_percentage(marks_list, max_per_subject=100):
    if not marks_list:
        return 0.0
    total = sum(marks_list)
    max_total = len(marks_list) * max_per_subject
    return round((total / max_total) * 100, 2)


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"


def calculate_result(percentage):
    return "PASS" if percentage >= 40 else "FAIL"


def highest_lowest(subjects, marks):
    if not marks:
        return None, None
    max_i = marks.index(max(marks))
    min_i = marks.index(min(marks))
    return (subjects[max_i], marks[max_i]), (subjects[min_i], marks[min_i])
