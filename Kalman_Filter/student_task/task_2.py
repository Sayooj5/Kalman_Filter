import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
# Task 2 
# Implement Linear Kalman Filter algorithm

# Subtask 1
# Define variables and algorithm of Linear Kalman Filter based on what you have learned in the lecture

# Timestep
dt = 0.04


class KF(object):
    def __init__(self, x) -> None:
        # initial state
        self.x = np.zeros(4).astype(float) if x is None else x

        # Covariance matrix of state estimate
        self.P = np.diag([1000, 1000, 1000, 1000])

        # State transition matrix
        self.F = np.array([[1, 0, dt, 0],
                           [0, 1, 0, dt],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]], dtype=np.float64)

        # Covariance matrix of process noise 
        self.Q = np.diag([0.1, 0.1, 0.1, 0.1]) ** 2

        # Measurement model
        self.H = np.array([[1, 0, 0, 0],
                           [0, 1, 0, 0]], dtype=np.float64)

        # Identical matrix
        self.I = np.eye(4)

        # Control Input matrix
        self.B = np.array([[(dt ** (2)) / 2, 0],
                           [0, (dt ** (2)) / 2],
                           [dt, 0],
                           [0, dt]])

        # Covariance matrix of observation noise
        self.R = np.diag([.1, .1]) ** 2

    # Prediction step by Kalman Filter

    def predict_kf(self, vx, vy):
        x = self.x
        F = self.F
        P = self.P
        Q = self.Q
        B = self.B

        #        Define control input vector
        u = np.array([[vx], [vy]], dtype=np.float64)

        new_x = F@x + B@u
        new_P = F@P@F.T + Q
        self.x = new_x
        self.P = new_P

        return self.x

    # Update step by Kalman Filter

    def update_kf(self, coord):
        x = self.x
        H = self.H
        R = self.R
        P = self.P
        I = self.I

        S = H@P@H.T + R 
        K = P@H.T@inv(S)
        L = coord - (H@x).T
        new_x = x + K@L.T
        new_P = (I - K@H)@P
        self.x = new_x
        self.P = new_P
        return self.x


# Subtask 2
# Define a function to filter measurements, based user input (kf/ekf) and return the filtering data
def Kalmanfilter(kf_class, meas, kf):
    filter_data = []
    for i in meas:
        if kf == "kf":

            filter_data.append(kf_class.predict_kf(i[2], i[3]))
            filter_data.append(kf_class.update_kf(i[:2]))

        else:

            filter_data.append(kf_class.predict_ekf(i[2], i[3]))
            filter_data.append(kf_class.update_ekf(i[:2]))

    return filter_data

    # Task 5 (Forecasting with linear KF):

    # Subtask 1
    # Define a function for forecasting with Linear Kalman Filter


def forecast_kf(f_dt, me): # f_dt is dt for forcasting
    F = np.array([[1, 0, f_dt, 0],
                  [0, 1, 0, f_dt],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])

    B = np.array([[(f_dt**2)/2, 0], [0, (f_dt**2)/2 ], [f_dt, 0], [0, f_dt]])
    u1 = []
    for i in me :
        x, y, vx, vy = i.squeeze()  # squeeze removes the singleton dimension of the array
        u1.append(np.array([[vx], [vy]]).T)
        arr_u = np.concatenate(u1).reshape(len(u1), 2, 1)

    forcast_points = []

    for m, j in zip(me, arr_u):
        # zip is being used to iterate over two iterables
        # write the equation for forecasting in for loop
        new_x = F @ m[:4] + B @ j
        forcast_points.append(new_x)

    return forcast_points


