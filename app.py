from flask import Flask, render_template_string
from datetime import date
import random

app = Flask(__name__)

list_class = (
    'Programming with C++',
    'Introduction to Computer Science',
    'Computer Ethics',
    'Calculus 2',
    'Discrete Structures and Computation',
    'Linear Algebra for Computer Science',
    'Academic Writing and Communication Skills',
    'Intro to French 2'
)

@app.route('/')
def study_today():
    chosen_class = random.choice(list_class)
    today = date.today()

    html = '''
    <!doctype html>
    <html lang="en">
    <head>
        <title>Today's Study Subject</title>
        <style>
            body { font-family: Arial; text-align: center; margin-top: 100px; }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <h1>{{ today }}</h1>
        <h2>📘 Study Today: <strong>{{ chosen_class }}</strong></h2>
    </body>
    </html>
    '''
    return render_template_string(html, today=today, chosen_class=chosen_class)

if __name__ == '__main__':
    app.run(debug=True)
