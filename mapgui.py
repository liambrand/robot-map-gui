from tkinter import Tk, Label, Button, Canvas
import math
import numpy as np
import matplotlib.pyplot as plt

class MapGUI:
    # Initialization
    def __init__(self, master):
        self.master = master
        master.title("Map GUI")
        master.geometry("150x150")

        #Buttons
        self.import_map_button = Button(master, text="Import Map", command = self.showMap)
        self.import_map_button.pack()

        self.read_text_button = Button(master, text="Read File", command = self.readData)
        self.read_text_button.pack()

        self.close_button = Button(master, text="Close", command = master.quit)
        self.close_button.pack()

    # Retrieve distance-angle pairs from a text file
    def readData(self):
        try:
          with open("coordinates.txt") as textFile:
            lines = [line.split() for line in textFile]
            # Values are read in as strings, so we convert them to ints
            for i in lines:
              i[0] = int(i[0])
              i[1] = int(i[1])
            return lines

        except IOError:
          print("Error reading file!")        



    # Draw map on plot
    def showMap(self):
        measurements = self.readData()
        print(measurements)
        coords = []
        x = []
        y = []

        # Turn distance-angle pairs into usable coordinates
        for measurement in measurements:
          x.append(self.getXCoord(measurement))
          y.append(self.getYCoord(measurement))

        plt.plot(x, y)
        plt.show()


    # Convert angles and measurements into a plot coordinate
    def getCoords(self, measurement):
        x = measurement[1] * math.cos(math.radians(measurement[0]))
        y = measurement[1] * math.sin(math.radians(measurement[0]))
        return x, y

    def getXCoord(self, measurement):
        x = measurement[1] * math.cos(math.radians(measurement[0]))
        return x

    def getYCoord(self, measurement):
        y = measurement[1] * math.sin(math.radians(measurement[0]))
        return y


root = Tk()
my_gui = MapGUI(root)
root.mainloop()
