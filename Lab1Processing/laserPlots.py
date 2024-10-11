import math
import matplotlib.pyplot as plt

ANGLE_INC = 0.00871450919657946

# Open and read the CSV file
with open('laser_content_line_cleaned.csv', 'r') as file:
    # Read the entire file as a string (assuming it's a single line)
    csv_data = file.read().strip()  # Remove any extra newline or spaces
    
    # Split the data into a list
    line_laser_dist = csv_data.split(',')

line_x = []
line_y = []

for index, dist in enumerate(line_laser_dist):
    if(dist == ''):
        continue

    print(dist)

    dist_f = float(dist)

    if(dist_f == 0.0):
        continue

    line_x.append(dist_f*math.cos(ANGLE_INC*index))
    line_y.append(dist_f*math.sin(ANGLE_INC*index))


# Open and read the CSV file
with open('laser_content_circle_cleaned.csv', 'r') as file:
    # Read the entire file as a string (assuming it's a single line)
    csv_data = file.read().strip()  # Remove any extra newline or spaces
    
    # Split the data into a list
    line_laser_dist = csv_data.split(',')

circle_x = []
circle_y = []

for index, dist in enumerate(line_laser_dist):
    if(dist == ''):
        continue

    print(dist)

    dist_f = float(dist)

    if(dist_f == 0.0):
        continue

    circle_x.append(dist_f*math.cos(ANGLE_INC*index))
    circle_y.append(dist_f*math.sin(ANGLE_INC*index))


# Open and read the CSV file
with open('laser_content_spiral_cleaned.csv', 'r') as file:
    # Read the entire file as a string (assuming it's a single line)
    csv_data = file.read().strip()  # Remove any extra newline or spaces
    
    # Split the data into a list
    line_laser_dist = csv_data.split(',')

spiral_x = []
spiral_y = []

for index, dist in enumerate(line_laser_dist):
    if(dist == ''):
        continue

    print(dist)

    dist_f = float(dist)

    if(dist_f == 0.0):
        continue

    spiral_x.append(dist_f*math.cos(ANGLE_INC*index))
    spiral_y.append(dist_f*math.sin(ANGLE_INC*index))


scan_figure = plt.figure('Scan')
plt.figure(scan_figure)

plt.subplot(1,3,1)
plt.scatter(line_x[:], line_y[:])
plt.scatter(0, 0)
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.title("Laser Scan Data for Line")

plt.subplot(1,3,2)
plt.scatter(circle_x[:], circle_y[:])
plt.scatter(0, 0)
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.title("Laser Scan Data for Circle")

plt.subplot(1,3,3)
plt.scatter(spiral_x[:], spiral_y[:])
plt.scatter(0, 0)
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.title("Laser Scan Data for Spiral")
plt.show()