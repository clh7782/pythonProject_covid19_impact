import pandas as pd
import plotly.graph_objects as go

import plotly.express as px

df = px.data.gapminder().query("year == 2007")

# px.scatter_geo location need to be ‘ISO-3’, ‘USA-states’, or ‘country names’
fig = px.scatter_geo(df, locations="iso_alpha",
                      size="gdpPercap",
                      color="country")
fig.show()