import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime, timedelta
import joblib

df = pd.read_csv("appointments.csv") 

df.dropna(inplace=True)
df['scheduled_time'] = pd.to_datetime(df['scheduled_time'])
df['actual_time'] = pd.to_datetime(df['actual_time'])

df['delay'] = (df['actual_time'] - df['scheduled_time']).dt.total_seconds() / 60

df['hour'] = df['scheduled_time'].dt.hour
df['day_of_week'] = df['scheduled_time'].dt.dayofweek

df['doctor_avg_delay'] = df.groupby('doctor_id')['delay'].transform('mean')

df['prev_patient_delay'] = df.groupby('doctor_id')['delay'].shift(1).fillna(0)

features = ['doctor_id', 'hour', 'day_of_week', 'doctor_avg_delay', 'prev_patient_delay']
target = 'delay'

X = df[features]
y = df[target]

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, 'wait_time_predictor.pkl')

def predict_wait_time(doctor_id, scheduled_time):
    """Predict expected delay for a given doctor and time."""
    model = joblib.load('wait_time_predictor.pkl')
    hour = scheduled_time.hour
    day_of_week = scheduled_time.weekday()
    doctor_avg_delay = df[df['doctor_id'] == doctor_id]['doctor_avg_delay'].mean()
    prev_patient_delay = df[df['doctor_id'] == doctor_id]['prev_patient_delay'].mean()
    return model.predict([[doctor_id, hour, day_of_week, doctor_avg_delay, prev_patient_delay]])[0]

scheduled_time = datetime(2024, 3, 26, 18, 30)
predicted_delay = predict_wait_time(doctor_id=5, scheduled_time=scheduled_time)
print(f"Expected wait time: {predicted_delay:.2f} minutes")
