import folium
import pandas



data = pandas.read_csv(r"C:\PythonProjects\MappingProject\file\Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

            
map = folium.Map(location=[38.58,-90.09],zoom_start=4, tiles="Mapbox Bright")

#featured group is use to add multiple markers on map
fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius = 6, popup=str(el)+" m",fill= True,fill_color=color_producer(el),color='blue', fill_opacity=0.7))


fgp = folium.FeatureGroup(name="Population")

#adding a GeoJson Polygon Layer
#fg.add_child(folium.GeoJson(open("world.json",encoding = "utf-8-sig").read()))
fgp.add_child(folium.GeoJson(data=open(r'C:\PythonProjects\MappingProject\file\world.json','r', encoding='utf-8-sig').read(),
                            style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                                        else 'orange' if 10000000 <=x['properties']['POP2005']< 20000000 else 'red'}))
    

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())#Adding Layer Control Panel

map.save("Map.html")


#map.add_child(folium.Marker(location=[38.2,-99.1], popup="Hi I am marker ",icon=folium.Icon(color='green')))

#fg.add_child(folium.Marker(location=[lt,ln],popup="Hi this is marker1",icon=folium.Icon(color='green')))

