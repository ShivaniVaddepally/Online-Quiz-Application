from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --------------- Quiz Questions ----------------
# We are storing questions in a Python list for simplicity
questions = [
    {
        "question": "What is Python?",
        "options": ["Snake", "Programming Language", "Car", "Game"],
        "answer": "Programming Language"
    },
    {
        "question": "HTML stands for?",
        "options": ["High Text", "Hyper Tool", "Hyper Text Markup Language", "Home Tool"],
        "answer": "Hyper Text Markup Language"
    },
    {
        "question": "CSS is used for?",
        "options": ["Styling Web Pages", "Programming Logic", "Database", "Server"],
        "answer": "Styling Web Pages"
    }
]

# --------------- Routes ----------------

# Home / Login page
@app.route('/')
def home():
    return render_template('login.html')

# Quiz page
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        for i, q in enumerate(questions):
            selected = request.form.get(str(i))
            if selected == q["answer"]:
                score += 1
        return render_template('result.html', score=score, total=len(questions))
    return render_template('quiz.html', questions=questions)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
