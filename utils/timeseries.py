import plotly.graph_objects as go
import plotly.express as px
import constants

import numpy as np


def fig_trendline_data(pdt, yvar, color, **kwargs):
    fig = px.scatter(
        pdt, 
        x=pdt.year, 
        y=pdt[yvar], 
        color_discrete_sequence=[color],
        trendline="ols"
    )
    return fig.data[1]

def fig_scatter_data(pdt, yvar, color, name, **kwargs):
    return go.Scattergl(
        x=pdt.year.astype(float),
        y=pdt[yvar].astype(float),
        marker_color=color,
        name=name,
        **kwargs
    )

def create(
    df,
    datafunc,
    yrange=[3.5,5], 
    ytitle="Mean Finish Time (h)", 
    legend_kws = dict(
        yanchor="bottom",
        y=0.01,
        xanchor="right",
        x=0.99
    ),
    figdt_kws={},
    **kwargs
):
    fig_dict = {
        "layout" : {},
        "data" : datafunc(df, **figdt_kws)
    }
    fig_dict["layout"]["xaxis"] = {
        "title": "Year", 
        "showgrid":False, 
        "range":[
            constants.SETTINGS["year_range"][0] - 1, 
            constants.SETTINGS["year_range"][1] + 1
        ]
    }
    fig_dict["layout"]["yaxis"] = {"title": ytitle, "showgrid":False, "range":yrange}

    fig = go.Figure(fig_dict)
    # fig.update_traces(hoverinfo='skip', hovertemplate=None)
    fig.update_layout(**constants.FIG_LAYOUT_DEFAULTS)
    fig.update_xaxes(
        showline=True, 
        linewidth=2, 
        linecolor='black', 
        ticks="outside", 
        tickwidth=2, 
        tickcolor='black', 
        ticklen=7
    )
    fig.update_yaxes(
        showline=True, 
        linewidth=2, 
        linecolor='black', 
        ticks="outside", 
        tickwidth=2, 
        tickcolor='black', 
        ticklen=7
    )
    fig.update_layout(
        legend=legend_kws,
        margin=dict(l=0,r=0,t=50,b=0,pad=20),
        **kwargs
    )
    return fig

def create_scatter_with_trend(df, color, yvar, **kwargs):
    def gen_fig_data(df):
        scatter = fig_scatter_data(
            df,
            yvar=yvar,
            color=color,
            name="",
            mode="markers"
        )
        trendline = fig_trendline_data(
            df,
            yvar=yvar,
            color=color
        )
        return [scatter, trendline]
    fig = create(
        df,
        gen_fig_data,
        **kwargs
    )
    fig.update_traces(showlegend=False)
    return fig

def create_timeseries_by_gender(
    gender, df, **kwargs
):
    return create_scatter_with_trend(
        df = df[df.gender == gender[0]].copy(),
        color = constants.GENDER_COLORS[gender],
        title= gender + " Runners",
        **kwargs
    )