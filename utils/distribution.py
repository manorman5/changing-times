import utils.utils as utils
import constants
import plotly.graph_objects as go

def create(
    df, 
    yrange, 
    datafunc, 
    xrange = [2.5, 6.5],
    xtitle = "Marathon Finish Time (h)"
):
    years = df.year.drop_duplicates().values.tolist()
    fig_dict = {
        "data": [],
        "layout": {},
        "frames": []
    }

    # fill in most of layout
    fig_dict["layout"]["xaxis"] = {"range": xrange, "title": xtitle, "showgrid":False}
    fig_dict["layout"]["yaxis"] = {"title": "Runner Density", "range":yrange, "showgrid":False}

    sliders_dict = {
        "active": 0,
        "yanchor": "top",
        "xanchor": "left",
        "currentvalue": {
            "visible": False,
        },
        "pad": {"b": 10, "t": 50},
        "len": 0.9,
        "x": 0.05,
        "y": 0,
        "steps": []
    }

    # create start data
    fig_dict["data"] = datafunc(df, years[0])

    # make frames
    fig_dict["frames"] = [{"data":datafunc(df, year), "name": str(year)} for year in years]
    sliders_dict["steps"].extend([ 
        {
            "args": [
                [str(year)],
                utils.frame_args(0)
            ],
            "label": str(year) + " - " + str(year + 4),
            "method": "animate"
        }
        for year in years
    ])

    fig_dict["layout"]["sliders"] = [sliders_dict]

    fig = go.Figure(fig_dict)

    fig.update_traces(hoverinfo='skip', hovertemplate=None)
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
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ),
        margin=dict(l=0,r=15,t=0,b=0,pad=0)
    )

    return fig

def fig_bin_data(dt, xvar, yvar, wvar, name, color):
    return go.Bar(
        x = dt[xvar],
        y = dt[yvar],
        width = dt[wvar],
        name = name,
        marker_color=color,
        marker_opacity=0.75,
        marker_line_color="black",
        marker_line_width=1.5
    )

def create_distribution_timeseries(df, color, yrange=[0,0.5], **kwargs):
    def bar_data_by_year(pdt, yr):
        dt = pdt[
            (pdt.year == yr)
        ].copy()
        return fig_bin_data(
            dt, 
            xvar="bin_center",
            yvar="density",
            wvar="bin_width",
            name="",
            color=color,
        )
    fig = create(
        df,
        yrange,
        bar_data_by_year,
        **kwargs
    )
    fig.update_traces(showlegend=False)
    return fig