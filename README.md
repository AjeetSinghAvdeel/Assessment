AI Solution for Peak Hour Patient Flow Management

Overview

The aim of this project is to minimize peak-hour wait times at Jayanagar Specialty Clinic through the utilization of AI-based appointment delay prediction and doctor schedule optimization. The solution implements machine learning for predicting the expected wait times and dynamically adjusting patient scheduling.

Problem Statement

The clinic has 40-minute average wait times for peak hours (5-8 PM), with patients waiting a maximum of 90 minutes.

Patients typically show up 20-30 minutes ahead of time, hoping to be attended to sooner.

Consultation lengths for doctors range from 8-22 minutes, causing volatile delays.

Recommended AI Solution

Major Features:

✅ Predicting Appointment Delay - Based on past data to forecast anticipated delays by doctor.
✅ Dynamic Slot Allocation - Dynamically adapts scheduling depending on real-time availability.
✅ Patient Arrival Prediction - Anticipates early arrivals and manages the queue more efficiently.
✅ SMS Notification - Informs patients of real-time estimated waiting times.

AI Model & Implementation

Data Processing:

Considers previous 3 months' appointment history.

Extracts doctor-wise average delays, peak-hour trends, and early arrival patterns.

Machine Learning Model:

Random Forest Regressor trained on:

Doctor ID

Hour of Appointment

Day of the Week

Doctor's Average Delay

Previous Patient's Delay

Predictive Scheduling Workflow:

Load previous appointment records.

Train the AI model to predict wait times.

Utilize predictions to schedule time slots dynamically.

Notify patients with expected wait times through real-time updates.

How to Run the Project

Clone this repository:

git clone https://github.com/PearlThoughtsInternship/AI-Internship-Interview-Assessment.git
cd AI-Internship-Interview-Assessment/Assessment1

Install dependencies:

pip install -r requirements.txt

Run the AI model:

python predict_wait_time.py

Example Usage:

from datetime import datetime
predicted_delay = predict_wait_time(doctor_id=5, scheduled_time=datetime(2024, 3, 26, 18, 30))
print(f"Expected wait time: {predicted_delay:.2f} minutes")

Expected Outcome

✅ Reduces wait times by at least 30%.
✅ Evenly distributes patient load across doctors.
✅ Enhances patient experience with better transparency.

Submission Instructions

Raise a Pull Request (PR) with your solution.

Record a short video explaining your approach.

Attach the video link in your submission form.

Share your PR link using the provided internship team's form.
