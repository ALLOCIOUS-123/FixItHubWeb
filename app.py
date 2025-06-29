from flask import Flask, render_template, request, jsonify
from flask_migrate import Migrate
from dotenv import load_dotenv
from models import db, Problem, Solution
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///fixithub.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Routes
@app.route('/')
def index():
    problems = Problem.query.order_by(Problem.created_at.desc()).all()
    return render_template('index.html', problems=problems)

@app.route('/api/problems', methods=['GET'])
def list_problems():
    problems = Problem.query.order_by(Problem.created_at.desc()).all()
    return jsonify([problem.to_dict() for problem in problems])

@app.route('/api/problems', methods=['POST'])
def create_problem():
    data = request.get_json()
    if not data or not all(key in data for key in ('title', 'description')):
        return jsonify({'error': 'Missing required fields'}), 400

    problem = Problem(title=data['title'], description=data['description'])
    db.session.add(problem)
    db.session.commit()
    return jsonify(problem.to_dict()), 201

@app.route('/api/problems/<int:problem_id>', methods=['GET'])
def get_problem(problem_id):
    problem = Problem.query.get_or_404(problem_id)
    return jsonify(problem.to_dict())

@app.route('/problem/<int:problem_id>', methods=['GET'])
def view_problem(problem_id):
    problem = Problem.query.get_or_404(problem_id)
    solutions = Solution.query.filter_by(problem_id=problem_id).order_by(Solution.votes.desc()).all()
    return render_template('problem.html', problem=problem, solutions=solutions)

@app.route('/api/problems/<int:problem_id>/solutions', methods=['POST'])
def add_solution(problem_id):
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing solution text'}), 400

    Solution.query.get_or_404(problem_id)  # Ensure problem exists
    solution = Solution(text=data['text'], problem_id=problem_id)
    db.session.add(solution)
    db.session.commit()
    return jsonify(solution.to_dict()), 201

@app.route('/api/problems/<int:problem_id>/solutions/<int:solution_id>/vote', methods=['POST'])
def vote_solution(problem_id, solution_id):
    solution = Solution.query.get_or_404(solution_id)
    solution.votes += 1
    db.session.commit()
    return jsonify(solution.to_dict())

# Run server
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # For development: ensure tables exist if not using `flask db upgrade`
    app.run(
        debug=os.getenv('FLASK_DEBUG', '1') == '1',
        host=os.getenv('FLASK_HOST', '127.0.0.1'),
        port=int(os.getenv('FLASK_PORT', '5000'))
    )