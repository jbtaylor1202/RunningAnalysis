import os
import os.path
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import tkinter as tk
import gpxpy
import matplotlib.pyplot as plt
import seaborn as sns
import gmplot
import datetime


print("Please select folder containing gpx files")
print("-----------------------")
window = tk.Tk()
window.withdraw()
folderName = askdirectory()
gpxFiles = os.listdir(folderName)
print("The selected directory was: " + folderName)
os.chdir(folderName)
print("-----------------------")
print("")
print(gpxFiles)

print("---START READING FILES---")

lat = []
lon = []


for runFile in gpxFiles:
    #Opens our .gpx file, then parses it into a format that is easy for us to run through
    gpx_file = open(runFile, 'r')
    gpx = gpxpy.parse(gpx_file)
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                lat.append(point.latitude)
                lon.append(point.longitude)
gpx_file.close()

print("---END READING FILES---")

#Start an instance of our map, with three arguments: lat/lon centre point of map - in this case,
#We'll use the first location in our data. The last argument is the default zoom level of the map
gmap = gmplot.GoogleMapPlotter(lat[0], lon[0], 20)

#Create our heatmap using our lat/lon lists for x and y coordinates
gmap.heatmap(lat, lon)

print("---DRAWING MAP---")
#Draw our map and save it to the html file named in the argument
runDate = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
gmap.draw(runDate + ".html")
print("---MAP SAVED TO CURRENT DIRECTORY---")

