from gmplot import gmplot
import random
import pandas as pd
import sys

file = sys.argv[1]
data = pd.read_csv(file)

x = list(data['Latitude'])
y = list(data['Longitude'])
size = len(x)
locations = [(x[i], y[i]) for i in range(size)]
random.shuffle(locations)

latmax = max(x)
lonmax = max(y)

latmin = min(x)
lonmin = min(y)
# chicago = 41.850029, -87.6500473
gmap = gmplot.GoogleMapPlotter(41.850029, -87.6500473, 13)
# Polygon
golden_gate_park_lats, golden_gate_park_lons = zip(*[
    (latmin, lonmax),
    (latmin, lonmin),
    (latmax, lonmin),
    (latmax, lonmax),
    (latmin, lonmax)
    ])
gmap.plot(golden_gate_park_lats, golden_gate_park_lons, 'cornflowerblue', edge_width=10)

# Scatter points
top_attraction_lats, top_attraction_lons = zip(*locations[:size / 100])
gmap.scatter(top_attraction_lats, top_attraction_lons, 'cornflowerblue', size=30, marker=False)

hidden_gem_lat, hidden_gem_lon = 41.850029, -87.6500473
gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')
# Draw
gmap.draw("my_map.html")