from flask import Flask, request, jsonify, render_template, redirect, url_for
from models import db, HealthData
from predict_model import predict_weight
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    height = float(request.form['height'])
    predicted_weight = predict_weight(height)
    return render_template('index.html', prediction=round(predicted_weight, 2))

@app.route('/track')
def track():
    return render_template('track.html')

@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.get_json()
    new_entry = HealthData(
        user_id=data['user_id'],
        height=data.get('height'),
        weight=data.get('weight'),
        steps=data.get('steps'),
        heart_rate=data.get('heart_rate'),
        bpm=data.get('bpm'),
        oxygen_level=data.get('oxygen_level'),
        mood=data.get('mood')
    )
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({'message': 'Data added successfully'}), 201

@app.route('/dashboard')
def dashboard():
    user_id = request.args.get('user_id', 'default_user')  # Simple user handling
    data = HealthData.query.filter_by(user_id=user_id).all()
    return render_template('dashboard.html', data=[d.to_dict() for d in data])

@app.route('/api/data/<user_id>')
def get_data(user_id):
    data = HealthData.query.filter_by(user_id=user_id).all()
    return jsonify([d.to_dict() for d in data])

if __name__ == '__main__':
    app.run(debug=True)