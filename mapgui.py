from tkinter import Tk, Label, Button, Canvas
import math
import numpy as np
import matplotlib.pyplot as plt

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Map GUI")
        master.geometry("150x150")

        #self.label = Label(master, text="Map GUI!")
        #self.label.pack()

        self.greet_button = Button(master, text="Import Map", command = self.showMap)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command = master.quit)
        self.close_button.pack()

        #self.mapCanvas = Canvas(master, width = 800, height = 1000)
        #self.mapCanvas.pack()

    def drawMap(self):
        toDraw = self.getMap()
        centerCanvas = [400, 500]        

        #self.mapCanvas.create_line(centerCanvas[0], centerCanvas[1], 100, 200)
        for x in toDraw:
          self.mapCanvas.create_line(centerCanvas[0] + x[0], centerCanvas[1] + x[1], 100, 100)

        #self.w.create_line(0, 0, 200, 100)
        #self.w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
        #self.w.create_rectangle(50, 25, 150, 75, fill="blue")
        
    def getMap(self):
        #print("Map Imported")
        measurements = [ [0, 100],
                      [90, 100],
                      [180, 100],
                      [270, 100]]
        print(measurements)
        return measurements

    def showMap(self):

        measurements = self.getMap()
        coords = []

        for measurement in measurements:
          x, y = self.getCoords(measurement)
          coords.append([x, y])

        for coord in coords:
          plt.plot(coord[0], coord[1], 'ro-')


        plt.show()

    def getCoords(self, measurement):
        x = measurement[1] * math.cos(math.radians(measurement[0]))
        y = measurement[1] * math.sin(math.radians(measurement[0]))
        return x, y
        



    def getXCoord(i):

        return i


    def getYCoord(i):

        return i


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
