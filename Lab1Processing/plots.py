import sys
import os

# Get the parent directory and add it to the path to access utilities
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

import matplotlib.pyplot as plt
from utilities import FileReader

imu_filenames = ['imu_content_line.csv', 'imu_content_circle.csv', 'imu_content_spiral.csv']
odom_filenames = ['odom_content_line.csv', 'odom_content_circle.csv', 'odom_content_spiral.csv']
line_plot = plt.figure('Line')
circle_plot = plt.figure('Circle')
spiral_plot = plt.figure('Spiral')

for imu_count, file in enumerate(imu_filenames):
    # Plot data for line    
    if imu_count == 0:
        plt.figure(line_plot)
    elif imu_count == 1:
        plt.figure(circle_plot)
    elif imu_count == 2:
        plt.figure(spiral_plot)

    headers, values=FileReader(file).read_file() 
    time_list=[]
    first_stamp=values[0][-1]
        
    for val in values:
        time_list.append(val[-1] - first_stamp)

    plt.subplot(1,3,1)

    for i in range(0, len(headers) - 1):
        plt.plot(time_list, [lin[i] for lin in values], label= headers[i]+ " linear")
        
        
    #plt.plot([lin[0] for lin in values], [lin[1] for lin in values])
    if imu_count == 0:
        plt.legend()
        plt.grid()
        plt.title('IMU Data for Line')
        plt.xlabel('Time (ns)')
        plt.ylabel(r'Linear Accelerations (m/$s^{2}$)/Angular Velocity (rad/s)')
    elif imu_count == 1:
        plt.legend()
        plt.grid()
        plt.title('IMU Data for Circle')
        plt.xlabel('Time (ns)')
        plt.ylabel(r'Linear Accelerations (m/$s^{2}$)/Angular Velocity (rad/s)')
    elif imu_count == 2:
        plt.legend()
        plt.grid()
        plt.title('IMU Data for Spiral')
        plt.xlabel('Time (ns)')
        plt.ylabel(r'Linear Accelerations (m/$s^{2}$)/Angular Velocity (rad/s)')

for odom_count, file in enumerate(odom_filenames):
    # Plot data for line    
    if odom_count == 0:
        plt.figure(line_plot)
    elif odom_count == 1:
        plt.figure(circle_plot)
    elif odom_count == 2:
        plt.figure(spiral_plot)

    headers, values=FileReader(file).read_file() 
    time_list=[]
    first_stamp=values[0][-1]
        
    for val in values:
        time_list.append(val[-1] - first_stamp)

    plt.subplot(1,3,2)

    for i in range(0, len(headers) - 1):
        plt.plot(time_list, [lin[i] for lin in values], label= headers[i]+ " linear")
        
        
    #plt.plot([lin[0] for lin in values], [lin[1] for lin in values])
    if odom_count == 0:
        plt.legend()
        plt.grid()
        plt.title('Odometry Data for Line')
        plt.xlabel('Time (ns)')
        plt.ylabel('Meters (m)/Meters (m)/Radians (rad)')
    elif odom_count == 1:
        plt.legend()
        plt.grid()
        plt.title('Odometry Data for Circle')
        plt.xlabel('Time (ns)')
        plt.ylabel('Meters (m)/Meters (m)/Radians (rad)')
    elif odom_count == 2:
        plt.legend()
        plt.grid()
        plt.title('Odometry Data for Spiral')
        plt.xlabel('Time (ns)')
        plt.ylabel('Meters (m)/Meters (m)/Radians (rad)')

for odom_xy_count, file in enumerate(odom_filenames):
    # Plot data for line    
    if odom_xy_count == 0:
        plt.figure(line_plot)
    elif odom_xy_count == 1:
        plt.figure(circle_plot)
    elif odom_xy_count == 2:
        plt.figure(spiral_plot)

    headers, values=FileReader(file).read_file() 
    time_list=[]
    first_stamp=values[0][-1]
        
    for val in values:
        time_list.append(val[-1] - first_stamp)

    plt.subplot(1,3,3)

    plt.plot([lin[0] for lin in values], [lin[1] for lin in values])
        
        
    #plt.plot([lin[0] for lin in values], [lin[1] for lin in values])
    if odom_xy_count == 0:
        plt.legend()
        plt.grid()
        plt.title('Odometry Data (X vs Y) for Line')
        plt.xlabel('Meters (m)')
        plt.ylabel('Meters (m)')
    elif odom_xy_count == 1:
        plt.legend()
        plt.grid()
        plt.title('Odometry Data (X vs Y) for Circle')
        plt.xlabel('Meters (m)')
        plt.ylabel('Meters (m)')
    elif odom_xy_count == 2:
        plt.legend()
        plt.grid()
        plt.title('Odometry Data (X vs Y) for Spiral')
        plt.xlabel('Meters (m)')
        plt.ylabel('Meters (m)')


plt.figure(line_plot)
plt.show()
plt.figure(circle_plot)
plt.show()
plt.figure(spiral_plot)
plt.show()
