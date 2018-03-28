import folium
import pandas

data = pandas.read_csv(r"C:\Users\abhil\AppData\Local\Programs\Python\Python36-32\PythonExample\MappingProject\Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[38.58,-90.09],zoom_start=5,tiles="Mapbox Bright")

#featured group is use to add multiple markers on map
fg = folium.FeatureGroup(name="My Map")
for lt,ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lt,ln],popup="Hi this is marker1",icon=folium.Icon(color='green')))

map.add_child(fg)

#map.add_child(folium.Marker(location=[38.2,-99.1], popup="Hi I am marker ",icon=folium.Icon(color='green')))
map.save("Map.html")
