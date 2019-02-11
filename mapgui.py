from tkinter import Tk, Label, Button, Canvas
import math
import numpy as np
import matplotlib.pyplot as plt

class MapGUI:
    def __init__(self, master):
        self.master = master
        master.title("Map GUI")
        master.geometry("150x150")

        self.import_map_button = Button(master, text="Import Map", command = self.showMap)
        self.import_map_button.pack()

        self.close_button = Button(master, text="Close", command = master.quit)
        self.close_button.pack()


    def drawMap(self):
        toDraw = self.getMap()
        centerCanvas = [400, 500]        

        for x in toDraw:
          self.mapCanvas.create_line(centerCanvas[0] + x[0], centerCanvas[1] + x[1], 100, 100)
        

    # Get map angles and distances from serial
    def getMap(self):
        measurements = [[0, 100],
                      [90, 100],
                      [180, 100],
                      [270, 100],
                      [360, 100]]
        return measurements

    # Draw map on plot
    def showMap(self):

        measurements = self.getMap()
        coords = []
        x = []
        y = []

        for measurement in measurements:
         # x, y = self.getCoords(measurement)
         # coords.append([x, y])
          x.append(self.getXCoord(measurement))
          y.append(self.getYCoord(measurement))

        #for coord in coords:
        #  plt.plot([coord[0], 100], [coord[1], 150], 'ro-')
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
