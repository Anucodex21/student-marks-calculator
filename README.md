# student-marks-calculator

# Marks Scanner — Student Marks Calculator

A full-stack Flask web app that takes a student's subject-wise marks
and calculates their percentage, grade, and pass/fail result — with
a sci-fi HUD-style interface and a SQLite database that stores every
past record.

## Features
- Add a student with any number of subjects (marks out of 100 each)
- Auto-calculates: total marks, percentage, grade (A+ / A / B / C / Fail), pass/fail
- Highlights highest and lowest scoring subject
- Radial HUD gauge showing percentage + grade visually
- All records saved permanently in SQLite (`students.db`)
- View, browse, and delete past records from the Records page

## Tech Stack
| Layer      | Tech                          |
|------------|-------------------------------|
| Frontend   | HTML, CSS (custom HUD theme), vanilla JS |
| Backend    | Python, Flask                 |
| Database   | SQLite (2 related tables: `students`, `subject_marks`) |

## Project Structure
```
student-marks-calculator/
├── app.py              # Flask routes (the backend)
├── calculator.py        # Pure grade/percentage logic
├── database.py           # All SQLite read/write functions
├── templates/
│   ├── base.html         # Shared layout
│   ├── index.html         # Input form
│   ├── result.html         # Result page with HUD gauge
│   └── history.html         # All past records
├── static/
│   └── style.css           # HUD styling
├── requirements.txt
└── .gitignore
```

## How it works (data flow)
```
Browser (form)  --POST-->  Flask route /calculate
                                  │
                                  ▼
                          calculator.py (does the math)
                                  │
                                  ▼
                          database.py (saves to SQLite)
                                  │
                                  ▼
                          result.html (renders back to browser)
```

## Setup & Run

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd student-marks-calculator

# 2. Create a virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

The SQLite database file (`students.db`) is created automatically
on first run — no manual setup needed.

## Grading Scale
| Percentage | Grade |
|------------|-------|
| 90 – 100   | A+    |
| 75 – 89    | A     |
| 60 – 74    | B     |
| 40 – 59    | C     |
| Below 40   | Fail  |

Pass mark: **40%**

## Author
Arjun Saxena 

