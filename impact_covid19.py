from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('data/03-03-2020.csv')
mean = df['Confirmed'].mean()
normlised_data_C = [value/df['Confirmed'].mean() + 10 for value in  df['Confirmed']]
normlised_data_D = [value/df['Confirmed'].mean()+3 if value != 0  else value for value  in df['Deaths']]
normlised_data_R = [value/df['Confirmed'].mean() + 3 if value != 0  else value for value  in df['Recovered']]

hoverdata1 = df['Country/Region'] + " - "+ ['Confirmed cases: ' + str(v) for v in df['Confirmed'].tolist()]
hoverdata2 = df['Country/Region'] + " - "+ ['Death: ' + str(v) for v in df['Deaths'].tolist()]
hoverdata3 = df['Country/Region'] + " - "+ ['Recovered: ' + str(v) for v in df['Recovered'].tolist()]
# text = df['Country/Region']
fig = make_subplots()
# df = pd.read_csv('data/03-03-2020.csv')
fig1 = go.Figure(data=go.Scattergeo(
        lon = df['Longitude'],
        lat = df['Latitude'],
    name = 'Confirmed cases',
        hovertext = hoverdata1,
        marker = dict(
            size =  normlised_data_C,
            opacity = 0.5,
            color = 'blue',
            line = dict(
                width=0,
                color='rgba(102, 102, 102)'
            ),
        ),
        ))

fig2 = go.Figure(data=go.Scattergeo(
        lon = df['Longitude'],
        lat = df['Latitude'],
    name = 'Deaths',
        hovertext = hoverdata2,
        marker = dict(
            size =  normlised_data_D,
            opacity = 0.5,
            color = 'red',
            line = dict(
                width=0,
                color='rgba(102, 102, 102)'
            ),
        ),
        ))


fig3= go.Figure(data=go.Scattergeo(
        lon = df['Longitude'],
        lat = df['Latitude'],
        hovertext = hoverdata3,
     name = 'Recovered',
        marker = dict(
            size =  normlised_data_R,
            opacity = 0.5,
            color = 'green',
            line = dict(
                width=0,
                color='rgba(102, 102, 102)'
            ),
        ),
        ))

fig.add_trace(fig1.data[0])
fig.add_trace(fig2.data[0])
fig.add_trace(fig3.data[0])

fig.update_layout(
        title = 'The global impact of COVID-19',
    legend=dict(
        itemsizing = "constant",
        font=dict(
            family="sans-serif",
            size=20,
            color="black"
        )
    )
)
fig.show()