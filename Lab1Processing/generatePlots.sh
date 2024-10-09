#!/bin/bash

# Run this file by sending the following command in the same directory as this file:
# bash generatePlots.sh

# Plot IMU data
python3 filePlotterLab1.py --files imu_content_circle.csv --title "IMU Data For Circle" --xLabel "Time (ns)" --yLabel "Linear Accelerations (m/s^2)/Angular Velocity (rad/s)"

python3 filePlotterLab1.py --files imu_content_line.csv --title "IMU Data For Line" --xLabel "Time (ns)" --yLabel "Linear Accelerations (m/s^2)/Angular Velocity (rad/s)"

python3 filePlotterLab1.py --files imu_content_spiral.csv --title "IMU Data For Spiral" --xLabel "Time (ns)" --yLabel "Linear Accelerations (m/s^2)/Angular Velocity (rad/s)"

# Plot Odom data
#...

# Plot laser scan data
# ...