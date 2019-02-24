import plotly.plotly as maps
from plotly import tools
import pandas as pd
import random
import sys

tools.set_credentials_file(username='Malandru', api_key='4WhX52yCfdoSzRjtheyb')

file = sys.argv[1]
print 'Reading', file
csv = pd.read_csv(file)

csv['text'] = csv['Block'] + '. ' + csv['Primary Type']
lon = random.shuffle(list(csv['Longitude']))
lat = random.shuffle(list(csv['Latitude']))

scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]

data = [dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = lon[:20],
        lat = csv[:20],
        text = csv['text'],
        mode = 'markers',
        marker = dict(
            size = 8,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(width = 1, color = 'rgba(102,102,102'),
            colorscale = scl,
            cmin = 0,
            color = 24524,
            cmax = 24524,
            colorbar = dict(tittle = 'Delitos de Chicago')
        )
    )]

layout = dict(
        title = 'Otro titulo que no se donde va',
        colorbar = True,
        geo = dict(
            scope = 'usa',
            projection = dict(type = 'albers usa'),
            showland = True,
            landcolor = 'rgb(250, 250, 250)',
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        )
    )

fig = dict(data = data, layout = layout)
maps.iplot(fig, validate = False, filename = 'Chicagotest')