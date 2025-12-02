from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HealthData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)  # Simple user identifier (e.g., email or ID)
    height = db.Column(db.Float, nullable=True)  # In cm
    weight = db.Column(db.Float, nullable=True)  # In kg
    steps = db.Column(db.Integer, nullable=True)
    heart_rate = db.Column(db.Integer, nullable=True)  # BPM
    bpm = db.Column(db.Integer, nullable=True)  # Assuming BPM is separate from heart rate (e.g., resting vs. active)
    oxygen_level = db.Column(db.Float, nullable=True)  # Percentage
    mood = db.Column(db.String(50), nullable=True)  # e.g., "Happy", "Sad"
    date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'height': self.height,
            'weight': self.weight,
            'steps': self.steps,
            'heart_rate': self.heart_rate,
            'bpm': self.bpm,
            'oxygen_level': self.oxygen_level,
            'mood': self.mood,
            'date': self.date.isoformat()
        }