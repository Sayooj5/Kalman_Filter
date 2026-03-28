# Multisensorial Systems – Kalman Filter Lab (Python)

Python lab project on multi-sensor data fusion and Kalman Filter variants for autonomous vehicle trajectory estimation.
---

## What it does

- Reads real vehicle trajectory data from CSV and builds measurement arrays for a **linear Kalman Filter (KF)** and an **Extended Kalman Filter (EKF)**. 
- Implements complete KF and EKF pipelines (prediction + update) for a vehicle state-space model.
- Filters noisy measurements and forecasts future vehicle positions and velocities.
- Visualizes noisy vs. filtered vs. forecasted trajectories, optionally over a background map image.

---

## How it is built

- Language: Python  
- Libraries: NumPy, Matplotlib, itertools (as required in the course).
- Core tasks:
  - Task 1: CSV parsing, grouping by vehicle ID, and building measurement vectors (including heading in radians).  
  - Tasks 2 & 3: Implementation of linear KF and EKF algorithms with correct state, control input `u`, and matrix `B`.
  - Task 4: Visualization of measurements, KF, and EKF results, including background image with meter-to-pixel conversion.
  - Task 5: Trajectory forecasting using KF/EKF, plus optional ADE (Average Displacement Error) metric.

---

## Why it is relevant

- Applies **sensor fusion and state estimation** concepts from autonomous driving to real trajectory data.
- Shows experience with **Kalman Filters (linear and extended)**, including modeling, implementation, and tuning.
- Demonstrates skills in **Python data handling, numerical computing, and visualization** for AV perception tasks.

---

## Typical usage

- Load trajectory dataset (CSV).  
- Build measurements for KF or EKF.  
- Run filtering and forecasting for a selected vehicle (ego car).  
- Visualize and compare noisy vs. filtered vs. forecasted trajectories, and (optionally) evaluate ADE.
