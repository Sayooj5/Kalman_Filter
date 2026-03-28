import numpy as np
from numpy.linalg import inv
from task_1 import *
from task_2 import *
from task_3 import *
from task_4 import *
# Task 3 
# Define Extended Kalman Filter algorithm

# Subtask 1
# Define parameters of Kalman Filter based on what you have learned in the lecture


# Jacobian of measurement model
JH = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])

# timestep
dt = 0.04


class EKF(object):
    def __init__(self, x) -> None:
        # initial state
        self.x = np.zeros(4) if x is None else x

        # state transition matrix
        self.F = np.array([[1, 0, dt, 0],
                           [0, 1, 0, dt],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])

        # Covariance matrix of process noise
        self.Q = np.diag([0.1, 0.1, 0.1, np.deg2rad(.1)]) ** 2

        # Covariance matrix of process noise
        self.P = np.diag([1000, 1000, 1000, 1000])

        # Covariance matrix of observation noise
        self.R = np.diag([.1, .1]) ** 2

        # Measurement model
        self.H = np.array([[1, 0, 0, 0],
                           [0, 1, 0, 0]])

        # Identity matrix
        self.I = np.eye(4)

    # Prediction step by Extended Kalman Filter

    def predict_ekf(self, v, h):
        x = self.x
        F = self.F
        Q = self.Q
        P = self.P

        # Jacobian of F
        JF = np.array([[1, 0, dt * np.cos(h), -dt * v * np.sin(h)],
                       [0, 1, dt * np.sin(h), dt * v * np.cos(h)],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]], dtype=np.float64)

        B = np.array([[np.cos(h) * dt, 0],
                      [np.sin(h) * dt, 0],
                      [0, dt], [1, 0]], dtype=np.float64)

        # Define Control Input
        u = np.array([[v], [h]]).T
        op1 = F @ x
        op2 = B @ u.T
        new_x = op1 + op2
        new_P = JF @ self.P @ JF.T + Q

        self.x = new_x
        self.P = new_P

        return self.x

    # Update step by Extended Kalman Filter

    def update_ekf(self, coord):
        x = self.x
        P = self.P
        R = self.R
        H = self.H
        I = self.I
        C1= H @ x
        C2 =coord - C1.T
        S = H @ P @ H.T + R
        K = P @ H.T @ inv(S)

        new_x = x + K @ C2.T
        new_P = (I - K @ H) @ P

        self.x = new_x
        self.P = new_P

        return self.x

# Task 5 (Forecasting with EKF):

# Subtask 1
# Define a function for forecasting with Extended Kalman Filter 


def forecast_ekf(me,h, mag_v,f_dt):

    u1 = []

    for j in range(0,len(h)):
        u1.append(np.array([[mag_v[j], h[j]]]).T)
        arr_u = np.concatenate(u1).reshape(len(u1),2,1)

    B1 = []

    for i in range(0,len(h)):
        B1.append(np.array([[np.cos(h[i])*f_dt,0],
                           [np.sin(h[i])*f_dt,0],
                           [0,f_dt],
                           [1,0]],np.float64))

    F= np.array([[1, 0, f_dt, 0],
                  [0, 1, 0, f_dt],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])

    forcast_points = []

#B1 populated by iterating through h, arr_u has more than 2 dimensions with new mag and h
    for m, b, u in zip(me, B1, arr_u):
        op1 = F @ m
        op2 = b @ u

# Write the equation for forecasting in this for loop

        new_x = op1+ op2

        forcast_points.append(new_x)

    return forcast_points


# A function that show forecating based on user choice (kf/ekf) 
def forecast(n, meas, kf, f_dt):
    forecast_points = []
    for i in range(n):
        if kf == "kf":
            forecast_points.extend(forecast_kf(f_dt, meas))
            # ...
        else:
            h = meas[:, 3]
            mag_v = meas[:, 2]
            forecast_points.extend(forecast_ekf(meas, h, mag_v, f_dt))
            # ...
    return forecast_points

