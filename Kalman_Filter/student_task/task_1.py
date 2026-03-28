# importing libraries 
import numpy as np
import csv
import math
import itertools
import pandas as pd


# Task 1 ( Reading the dataset )

# Subtask 1
# Define a function that read data from a csv file


def read(filepath, filename):
    data = []
    with open(filepath + '/' + filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)

    return data


# Subtask 2
# Define a function that take the data as an input and creates measurements as a 2d Numpy array

def variable(data, kf):
    # Group data by ID
    groups = itertools.groupby(data, key=lambda x: x[0])

    # make a condition whether its kf or ekf
    if kf == "kf":

        # Extract elements that you need for the measurements (based on lecture, space state model for KF) 
        lst = [[[item[2], item[3], item[4], item[5]] for item in group] for _, group in groups]

        # Extract ego car (first car) and reshape the measurements                                                                                  
        meas = np.array(lst[0]).astype(float)

        return meas

    else:
        # Do the same method for EKF,you also need heading value for calculation  

        lst = [[[item[2], item[3], item[4], item[5],item[6]] for item in group] for _, group in groups]
        # Extract elements from lst
        x, y, vx, vy, h = np.array(lst[0]).T
        h = np.radians(h.astype(float))
        x = x.astype(float)
        y = y.astype(float)
        vx = vx.astype(float)
        vy = vy.astype(float)
        # Calculate the magnitude of velocity
        mag_v = np.sqrt(np.square(vx) + np.square(vy))

        # Creat measurements based on our assumption ( space state model for EKF ) then reshape the data
        meas = np.vstack((x, y, mag_v, h)).T
        

        return mag_v, h, meas


