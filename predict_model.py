import pickle
from sklearn.linear_model import LinearRegression
import numpy as np

# Dummy training data (height in cm, weight in kg) - replace with real data for accuracy
heights = np.array([150, 160, 170, 180, 190]).reshape(-1, 1)
weights = np.array([50, 60, 70, 80, 90])

# Train and save model
model = LinearRegression()
model.fit(heights, weights)
with open('weight_model.pkl', 'wb') as f:
    pickle.dump(model, f)

def predict_weight(height):
    with open('weight_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model.predict(np.array([[height]]))[0]