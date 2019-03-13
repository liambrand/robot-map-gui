from tkinter import Tk, Label, Button, Canvas
import bitarray
import glob
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
        
        self.read_binary_button = Button(master, text="Read Binary", command = self.readBinary)
        self.read_binary_button.pack()

        self.close_button = Button(master, text="Close", command = master.quit)
        self.close_button.pack()

    # Retrieve distance-angle pairs from a text file
    def readData(self):
        coords = []
        with open("./binarycoords/coords.bin", "rb") as f:
          try:
            while True:
              # Read in the bits according to the LIDAR response structure
              quality = f.read(6)
              inverseStart = f.read(1)
              start = f.read(1)
              angle_first = f.read(7)
              checkbit = f.read(1)
              angle_second = f.read(8)
              distance = f.read(16)

              # Append the angle_q6 bits
              angle = (b"".join([angle_first, angle_second]))

              # Turn binary into decimal
              # 'Actual heading = angle_q6/64.0 Degree'
              angle = (int(angle, 2) / 64.0)
              # 'Actual Distance = distance_q2/4.0 mm'
              distance = (int(distance, 2) / 4.0)/100
                    
              print(f'''Angle: {angle} \n
                      Distance: {distance}''')

              coord = [angle, distance]
              coords.append(coord)

          except:
              print('Done Reading')
        print(coords)
        return coords
   

    def readBinary(self):
      coords = []
      # For all files...
      with open("./binarycoords/coords.bin", "rb") as f:
          try:
            while True:
              # Read in the bits according to the LIDAR response structure
              quality = f.read(6)
              inverseStart = f.read(1)
              start = f.read(1)
              angle_first = f.read(7)
              checkbit = f.read(1)
              angle_second = f.read(8)
              distance = f.read(16)

              # Append the angle_q6 bits
              angle = (b"".join([angle_first, angle_second]))

              # Turn binary into decimal
              # 'Actual heading = angle_q6/64.0 Degree'
              angle = (int(angle, 2) / 64.0)
              # 'Actual Distance = distance_q2/4.0 mm'
              distance = (int(distance, 2) / 4.0)/100
                    
              print(f'''Angle: {angle} \n
                      Distance: {distance}''')

              coord = [angle, distance]
              coords.append(coord)

              print(coords)
              return coords

          except:
              print('Done Reading')
          
          

    # Draw map on plot
    def showMap(self):
        #measurements = self.readData()
        measurements = self.readBinary()
        print(measurements)
        coords = []
        x = []
        y = []

        # Turn distance-angle pairs into usable coordinates
        for measurement in measurements:
          x.append(self.getXCoord(measurement))
          y.append(self.getYCoord(measurement))

        plt.scatter(x, y)
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
