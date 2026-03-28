import task_1
import task_2
import task_3
from task_1 import *
from task_2 import *
from task_3 import *
from task_4 import *
import pandas as pd
import numpy as py
from numpy.linalg import inv

# Example Visualization (given later)
# from script_4 import Visualizer

# read data
data = task_1.read(filepath="D:/multi/dataset", filename="tracks_08.csv")

# Image background path
path = "D:/multi/dataset/08_background.png"

kf = "kf"  # Options are: "kf" or "ekf"
forecasting = True

# condition if kf is true or false , if its true just use line 25 if its false use 27 and 30
if kf == "kf":
    meas = variable(data, kf)  # defining variables for linear kf
    kf_class = KF(x=meas[0])  # Using Linear Kalman Filter
    value_df = pd.DataFrame(meas, columns=['xCenter', 'yCenter', 'xVel', 'yVel'], dtype=float)
    filter_data = Kalmanfilter(kf_class, meas, kf)
    filter1 = pd.concat([pd.DataFrame(i.T, columns=['xCenter', 'yCenter', 'xVel', 'yVel']) for i in filter_data], ignore_index=True)
else:
    mag_v, h, meas = variable(data, kf)  # defining variables for ekf
    kf_class = EKF(x=meas[0])  # Using Extended Kalman Filter
    value_df = pd.DataFrame(meas, columns=['xCenter', 'yCenter', 'mag_v', 'h'], dtype=float)
    filter_data = Kalmanfilter(kf_class, meas, kf)
    filter1 = pd.concat([pd.DataFrame(i, columns=['xCenter', 'yCenter', 'mag_v', 'h']) for i in filter_data], ignore_index=True)

meas_df = pd.DataFrame(meas, columns=['xCenter', 'yCenter', 'a', 'b'])
nmeas = []
filter1 = filter1.astype(float)






# forcasting with Linear KF or EKF 

# timestep for forcasting
f_dt = 0.02
# number of iteration for forecasting 
n = 5

#if forecasting == True:

forecast_points = forecast(n, meas, kf, f_dt)
forecast1 = pd.DataFrame(columns=['xCenter', 'yCenter', 'a', 'b'])
for i in forecast_points :
    row_df= pd.DataFrame(i, columns=['xCenter', 'yCenter', 'a', 'b'])
    forecast1 = forecast1._append(row_df,ignore_index=True)

forecastx = forecast1['xCenter'].values
forecasty = forecast1['yCenter'].values
forecastx1= []
forecasty1 = []

for i in range(1,len(forecastx),4):
    forecastx1.append(forecastx[i])

for i in range(1,len(forecasty),4):
    forecasty1.append(forecasty[i])


# Task 4: Visualization
# add your own visualization fucntion here
# Extract item[2] and item[3] from each row
#task_1
x_val = value_df['xCenter'].values
y_val = value_df['yCenter'].values

title= 'Kalman Forecast'

fx_val = filter1['xCenter'].values
fy_val = filter1['yCenter'].values




#plot_with_background(x_values,x_val,y_values,y_val, title, path)
start_index = 65
end_index = 75

FilteredGraph(fx_val[start_index-50:end_index], forecastx1[end_index:end_index+30], fy_val[start_index-50:end_index], forecasty1[end_index:end_index+30], title, path)

plt.show()


# add your ADE calculation for the forecast here    


# Example Visualization (given later)
#vis = Visualizer(data=data,filter_data=filter_data,forecast_points= forecast_points,background_path=path, mini=0, maxi=10000, interval=40, blit=False )
#vis = Visualizer(data, filter_data, forecast_points)
#vis.plot()





