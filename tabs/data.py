import constants
import utils.utils as utils

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import plotly
import plotly.graph_objects as go
import plotly.express as px

import pandas as pd
import numpy as np

geo_dist = pd.read_csv(constants.DATA_DIR + "/" + utils.get_filename(
    typep="geographic_distribution",
    contents="",
    modifier="",
    race_group="",
    speed=""
))

region_state_cw = geo_dist[["postal","region","state"]].drop_duplicates()

data_about = """#### Explore Where the Runners Ran
I gathered over 6 million marathoner results from the United States dating back
to 1900. I then cleaned the data in a multi step process. I dropped results with suspect finish times or missing racer demographics. I then 
tested the integrity of races' finish time distributions to ensure cleaning steps did not alter the distributions in any statistically 
significant way. The goal of this process is to ensure all races included in the analysis have trustworthy finish 
time distributions. Lastly, I restricted the dataset to years between 1995 and 2019; there are very few races in the 
dataset before 1995. Above, you can explore where the racers in the cleaned dataset ran. 
"""

def layout(yearmin, yearmax):
    return dcc.Tab(
        label='The Data', 
        children=[
            html.Div(className="row", children=[
                html.Div(
                    className="eight columns pretty_container", 
                    children=[
                        dcc.Graph(id='map')
                    ]
                ),
                html.Div(
                    className="four columns pretty_container", 
                    children=[
                        dcc.Graph(id='geo-sunburst')
                    ]
                )   
            ]),
            html.Div([
                html.Div([
                    html.P('Select years', className="control_label"),
                    dcc.RangeSlider(
                        id='by-geo-year-dropdown',
                        value=[yearmin, yearmax],
                        min=yearmin, 
                        max=yearmax,
                        marks={i: str(i) for i in range(yearmin, yearmax+1, 3)}
                    ),
                ], className="six columns pretty_container"),
                html.Div([
                    html.P('Select genders', className="control_label"),
                    dcc.Dropdown(
                        id='by-geo-gender-selector',
                        placeholder='Select genders',
                        options=[
                            {'label': 'Male', 'value': "M"},
                            {'label': 'Female', 'value': "F"},
                        ],
                        value=["M", "F"],
                        multi=True
                    ),
                ], className="three columns pretty_container"),
            ], className="row",id="by-geo-control-panel"),
            html.Hr(),
            dcc.Markdown(
                children=data_about
            )
        ]
    )

def filter_data(years, genders):
    return geo_dist[
        geo_dist.year.isin(years) & geo_dist.gender.isin(genders)
    ][["state","region","postal","event_name","lat","lon","freq"]].groupby(["state","postal","region","lat","lon","event_name"]).sum().reset_index()   

def create_map(plot_dt):
    fig = go.Figure()
    for region in region_state_cw.region.drop_duplicates():
        pdt = region_state_cw[
            region_state_cw['region'] == region
        ]
        locations = pdt.postal.values.tolist()
        if region == "West" and "MT" not in locations:
            locations = locations + ["MT"]

        color = constants.REGION_COLORS[region]
        fig.add_choropleth(
            locations=locations,
            locationmode="USA-states",
            z=[.5,] * len(locations), 
            showlegend=True, 
            name=region,
            colorscale= ((0.0, color), (1.0, color)), 
            showscale=False,
            marker_opacity=0.25,
            marker_line_color='white',
        )
    fig.update_traces(hoverinfo='skip', hovertemplate=None, showlegend=False)
    
    fig.add_scattergeo(
        lon = plot_dt['lon'],
        lat = plot_dt['lat'],
        text = plot_dt["event_name"] + " Marathon, " + plot_dt["state"] + " <br>" + "Number of Racers: "+ plot_dt["freq"].apply(lambda x: format(x,",")),
        mode = 'markers',
        marker = dict(
            color=plotly.colors.qualitative.Dark24[9],
            opacity=0.15,
            size=plot_dt["freq_norm"],
            line=dict(
                color='white',
                width=2
            )
        ),
        hoverinfo = "text"
    )

    fig.update_layout(
        geo = dict(
            scope='usa',
            projection=go.layout.geo.Projection(type = 'albers usa'),
            showlakes=True, # lakes
            lakecolor=constants.FIG_LAYOUT_DEFAULTS["plot_bgcolor"],
            bgcolor= constants.FIG_LAYOUT_DEFAULTS["plot_bgcolor"]
        ),
        margin=dict(l=0,r=0,t=0,b=0,pad=0),
    )
    fig.update_layout(**constants.FIG_LAYOUT_DEFAULTS)
    return fig

def create_geo_sunburst(plot_dt):
    regions = plot_dt.groupby("region").sum()[["freq"]].reset_index()
    states = plot_dt.groupby(["region","state"]).sum()[["freq"]].reset_index()
    
    parents = [""]*regions.shape[0] 
    labels = regions.region.values.tolist() 
    values = regions.freq.values
    colors = [constants.REGION_COLORS[rg] for rg in labels]

    parents = parents + states.region.values.tolist() 
    labels = labels + states.state.values.tolist() 
    values = np.concatenate((values, states.freq.values))
    colors = colors + [
        constants.REGION_COLORS[rg] for rg in states.region.values.tolist()
    ]
    
    parents = parents + plot_dt.state.values.tolist()
    labels = labels + [
        ee + "    " 
        if ee in states.state.values.tolist() 
        else ee 
        for ee in plot_dt.event_name.values.tolist()
    ]
    values = np.concatenate((values, plot_dt.freq.values))
    colors = colors + [
        constants.REGION_COLORS[rg] for rg in plot_dt.region.values.tolist()
    ]
    
    fig = go.Figure(
        go.Sunburst(
            parents=parents,
            labels=labels,
            values=values,
            marker=dict(
                colors=colors
            ),
            customdata=np.stack([values], axis=-1),
            hovertemplate='<b>%{label}</b><br> Numer of Runners: %{customdata[0]:,}<extra></extra>',
            branchvalues="total"
        )
    )
    fig.layout = go.Layout(**constants.FIG_LAYOUT_DEFAULTS)
    return fig