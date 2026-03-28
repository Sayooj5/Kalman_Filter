import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
# Task 4 (Visualisation)

# Subtask 1
def plot_coordinates(x, y, title):
    fig, ax = plt.subplots()
    ax.plot(x, y, 'bo', markersize=5)
    ax.set(xlabel='x', ylabel='y', title=title)
    ax.grid(True)
    plt.show()

# Subtask 2 (Visualization with background image)

#def plot_with_background(x2, y2, title,path ):
def FilteredGraph(fx_Val, forecastx1, fy_Val, forecasty1, title, path):
    # Read the background image
    background_img = Image.open(path)

    # Get the size of the image
    img_width, img_height = background_img.size

    # Calculate the aspect ratio
    aspect_ratio = img_width / img_height

    # Calculate the required crop dimensions based on the graph limits
    crop_left, crop_right, crop_bottom, crop_top = [factor * size for factor, size in zip([0.33, 0.93, 0.15, 0.95], [img_width, img_width, img_height, img_height])]


    # Crop the image to fit the graph
    cropped_img = background_img.crop((crop_left, crop_bottom, crop_right, crop_top))

    # Create a new plot
    fig, ax = plt.subplots()

    # Set the cropped image as the background of the plot
    ax.imshow(cropped_img, extent=[48, 90, -60, -20], aspect=aspect_ratio)

    # Plot first set of coordinates unfiltered
    plt.plot(fx_Val, fy_Val, 'ro', markersize=2)
    plt.plot(forecastx1, forecasty1, 'go', markersize=2)


    # Set the plot labels and title
    ax.set_xlabel('X coordinates')
    ax.set_ylabel('Y coordinates')
    ax.set_title(title)

    # Set the plot limits
    ax.set_xlim(50, 90)
    ax.set_ylim(-60, -20)

    # Show the plot
    plt.show()