# AI Solution for Managing Peak Hour Patient Flow

## Overview
This project aims to reduce peak-hour wait times at **Jayanagar Specialty Clinic** by leveraging AI to predict appointment delays and optimize doctor schedules. The solution uses **machine learning** to predict expected wait times and dynamically adjust patient scheduling.

## Problem Statement
- The clinic experiences **40-minute average wait times** during peak hours (5-8 PM), with some patients waiting up to **90 minutes**.
- Patients often arrive **20-30 minutes early**, expecting to be seen earlier.
- Doctor consultation durations vary from **8-22 minutes**, leading to unpredictable delays.

## Proposed AI Solution
### Key Features:
✅ **Appointment Delay Prediction** - Uses historical data to predict expected delays per doctor.
✅ **Dynamic Slot Allocation** - Adjusts scheduling based on real-time availability.
✅ **Patient Arrival Forecasting** - Predicts early arrivals and optimizes the queue.
✅ **SMS Notifications** - Updates patients on real-time estimated wait times.

## AI Model & Implementation
### Data Processing:
- Uses past **3 months of appointment records**.
- Extracts **doctor-wise average delays, peak-hour trends, and early arrival patterns**.

### Machine Learning Model:
- **Random Forest Regressor** trained on:
  - Doctor ID
  - Hour of Appointment
  - Day of the Week
  - Doctor’s Average Delay
  - Previous Patient’s Delay

### Predictive Scheduling Workflow:
1. **Load past appointment records**.
2. **Train the AI model** to forecast wait times.
3. **Use predictions** to optimize time slots dynamically.
4. **Notify patients** of expected wait times via real-time updates.

## How to Run the Project
1. **Clone this repository:**
   ```sh
   git clone https://github.com/PearlThoughtsInternship/AI-Internship-Interview-Assessment.git
   cd AI-Internship-Interview-Assessment/Assessment1
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the AI model:**
   ```sh
   python predict_wait_time.py
   ```
4. **Example Usage:**
   ```python
   from datetime import datetime
   predicted_delay = predict_wait_time(doctor_id=5, scheduled_time=datetime(2024, 3, 26, 18, 30))
   print(f"Expected wait time: {predicted_delay:.2f} minutes")
   ```

## Expected Outcome
✅ **Reduces wait times by at least 30%**.
✅ **Evenly distributes patient load across doctors**.
✅ **Enhances patient experience with better transparency**.

## Submission Instructions
1. **Raise a Pull Request (PR)** with your solution.
2. **Record a short video** explaining your approach.
3. **Attach the video link in your submission form**.
4. **Submit your PR link** in the form provided by the internship team.

---
🔹 **Author**: Ajeet Singh Avdeel  
🔹 **Internship Submission for AI Assessment #1**  

🚀 **Let’s optimize patient flow with AI!**

