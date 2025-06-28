from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    solutions = db.relationship('Solution', backref='problem', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'solutions': [solution.to_dict() for solution in self.solutions]
        }

class Solution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    votes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    problem_id = db.Column(db.Integer, db.ForeignKey('problem.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'votes': self.votes,
            'created_at': self.created_at.isoformat()
        }
