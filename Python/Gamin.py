#GPXPY makes using .gpx files really easy
import gpxpy

#Visualisation libraries
import matplotlib.pyplot as plt
import seaborn as sns

#Opens our .gpx file, then parses it into a format that is easy for us to run through
gpx_file = open('activity_2484178059.gpx', 'r')
gpx = gpxpy.parse(gpx_file)

gpx.tracks[0].segments[0].points[0]


lat = []
lon = []

for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            lat.append(point.latitude)
            lon.append(point.longitude)


fig = plt.figure(facecolor = '0.1')
ax = plt.Axes(fig, [0., 0., 1., 1.], )
ax.set_aspect('equal')
ax.set_axis_off()
fig.add_axes(ax)
plt.plot(lon, lat, color = 'deepskyblue', lw = 0.3, alpha = 0.9)
plt.show()

#Import the module first


#Start an instance of our map, with three arguments: lat/lon centre point of map - in this case,
#We'll use the first location in our data. The last argument is the default zoom level of the map
gmap = gmplot.GoogleMapPlotter(lat[0], lon[0], 20)

#Create our heatmap using our lat/lon lists for x and y coordinates
gmap.heatmap(lat, lon)

#Draw our map and save it to the html file named in the argument
gmap.draw("Player1.html")
