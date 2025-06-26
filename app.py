from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

problems = []

@app.route('/')
def index():
    return render_template('index.html', problems=problems)

@app.route('/add', methods=['POST'])
def add_problem():
    title = request.form['title']
    description = request.form['description']
    problems.append({
        'title': title,
        'description': description,
        'solutions': []
    })
    return redirect(url_for('index'))

@app.route('/problem/<int:pid>')
def view_problem(pid):
    problem = problems[pid]
    return render_template('problem.html', problem=problem, pid=pid)

@app.route('/problem/<int:pid>/add_solution', methods=['POST'])
def add_solution(pid):
    solution = request.form['solution']
    problems[pid]['solutions'].append({'text': solution, 'votes': 0})
    return redirect(url_for('view_problem', pid=pid))

@app.route('/problem/<int:pid>/vote/<int:sid>')
def vote_solution(pid, sid):
    problems[pid]['solutions'][sid]['votes'] += 1
    return redirect(url_for('view_problem', pid=pid))

if __name__ == '__main__':
    app.run(debug=True)
