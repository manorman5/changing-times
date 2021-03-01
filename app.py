import tabs.data as data
import tabs.age as age
import tabs.fast as fast
import tabs.intro as intro
import tabs.slow as slow

import constants
import utils.utils as utils
import utils.timeseries as timeseries
import utils.distribution as distribution

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc 

import os


app = dash.Dash(__name__, external_stylesheets = [])
port = int(os.environ.get("PORT", 5000))

app.layout = html.Div(
    className='app-body', 
    children=[
        dcc.Tabs(
            id = "tabs",
            children=[
                intro.Layout().get(),
                age.Layout().get(),
                fast.Layout().get(),
                slow.Layout().get(),
                data.layout(
                    yearmin=constants.SETTINGS["year_range"][0], 
                    yearmax=constants.SETTINGS["year_range"][1]
                )
            ]
        )
    ]
)


@app.callback(
    [
        Output('slow-whole-time-dist','figure'),
        Output('slow-whole-time-timeseries','figure'),
        Output('slow-proportion-by-race-timeseries','figure'),
        Output('slow-number-slow-timeseries','figure')
    ],
    [
        Input('slow-whole-time-gender-selector',"value"), 
        Input("slow-whole-time-race-dropdown","value"), 
        Input('slow-proportion-by-race-gender-selector',"value"), 
        Input("slow-proportion-by-race-race-dropdown","value"), 
        Input('slow-number-slow-gender-selector',"value"), 
        Input("slow-number-slow-race-dropdown","value"), 
    ]
)
def update_slow(gender, race, gender_prop, race_prop, gender_freq, race_freq):
    prop_timeseries = utils.create_fig_by_gender_and_by_race(
        slow.proportion_timeseries_testages_slow,
        race_prop,
        gender_prop,
        timeseries.create_scatter_with_trend,
        yvar = "proportion_demeaned",
        yrange = [-200,200],
        ytitle = "Demeaned % Difference"
    )
    freq_timeseries = utils.create_fig_by_gender_and_by_race(
        slow.runnerfreq_timeseries_testages_slow,
        race_freq,
        gender_freq,
        timeseries.create_scatter_with_trend,
        yvar = "freq",
        yrange = [
            0,
            slow.runnerfreq_timeseries_testages_slow[
                (slow.runnerfreq_timeseries_testages_slow.event_name == race_freq)
            ].freq.max()
        ],
        ytitle = 'Number of "slow" Runners'
    )
    
    time_dist = utils.create_fig_by_gender_and_by_race(
        slow.finish_distribution_testages_slow,
        race, 
        gender,
        distribution.create_distribution_timeseries,
        xrange=[4,6.5],
        yrange=[0,1]
    )
    time_timeseries = utils.create_fig_by_gender_and_by_race(
        slow.finish_timeseries_testages_slow,
        race, 
        gender,
        timeseries.create_scatter_with_trend,
        yvar="meantime",
        yrange=[4.5*60,6.5*60],
        ytitle="Mean Finish Time (min)",
        height=230
    )
    return time_dist, time_timeseries, prop_timeseries, freq_timeseries

@app.callback(
    [
        Output('fast-whole-time-dist','figure'),
        Output('fast-whole-time-timeseries','figure'),
        Output('fast-proportion-by-race-timeseries','figure'),
        Output('fast-number-fast-timeseries','figure')
    ],
    [
        Input('fast-whole-time-gender-selector',"value"), 
        Input("fast-whole-time-race-dropdown","value"), 
        Input('fast-proportion-by-race-gender-selector',"value"), 
        Input("fast-proportion-by-race-race-dropdown","value"), 
        Input('fast-number-fast-gender-selector',"value"), 
        Input("fast-number-fast-race-dropdown","value"), 
    ]
)
def update_fast(gender, race, gender_prop, race_prop, gender_freq, race_freq):
    prop_timeseries = utils.create_fig_by_gender_and_by_race(
        fast.proportion_timeseries_testages_fast,
        race_prop,
        gender_prop,
        timeseries.create_scatter_with_trend,
        yvar = "proportion_demeaned",
        yrange = [-200,200],
        ytitle = "Demeaned % Difference"
    )
    freq_timeseries = utils.create_fig_by_gender_and_by_race(
        fast.runnerfreq_timeseries_testages_fast,
        race_freq,
        gender_freq,
        timeseries.create_scatter_with_trend,
        yvar = "freq",
        yrange = [
            0,
            fast.runnerfreq_timeseries_testages_fast[
                (fast.runnerfreq_timeseries_testages_fast.event_name == race_freq)
            ].freq.max()
        ],
        ytitle = 'Number of "strong" Amatuers',
    )
    
    time_dist = utils.create_fig_by_gender_and_by_race(
        fast.finish_distribution_testages_fast,
        race, 
        gender,
        distribution.create_distribution_timeseries,
        xrange=[2.45,3.1]
    )
    time_timeseries = utils.create_fig_by_gender_and_by_race(
        fast.finish_timeseries_testages_fast,
        race, 
        gender,
        timeseries.create_scatter_with_trend,
        yvar="meantime",
        yrange=[2.25*60,3.25*60],
        ytitle="Mean Finish Time (min)",
        height=230
    )
    return time_dist, time_timeseries, prop_timeseries, freq_timeseries



@app.callback(
    [
        Output('age-age-dist','figure'),
        Output('age-age-timeseries','figure'),
        Output('age-time-dist','figure'),
        Output('age-time-timeseries','figure')
    ],
    [
        Input('age-age-gender-selector',"value"), 
        Input("age-age-race-dropdown","value"), 
        Input('age-time-gender-selector',"value"), 
        Input("age-time-race-dropdown","value"), 
    ]
)
def update_age(age_gender, age_race, time_gender, time_race):
    age_dist = utils.create_fig_by_gender_and_by_race(
        age.age_distribution,
        age_race, 
        age_gender,
        distribution.create_distribution_timeseries,
        xrange = [15,86],
        xtitle="Age"
    )
    age_timeseries = utils.create_fig_by_gender_and_by_race(
        age.age_timeseries,
        age_race, 
        age_gender,
        timeseries.create_scatter_with_trend,
        yvar="average_age",
        ytitle="Mean Runner Age",
        yrange=[30,55],
        height=230
    )
    time_dist = utils.create_fig_by_gender_and_by_race(
        age.finish_distribution_testages,
        time_race, 
        time_gender,
        distribution.create_distribution_timeseries
    )
    time_timeseries = utils.create_fig_by_gender_and_by_race(
        age.finish_timeseries_testages,
        time_race, 
        time_gender,
        timeseries.create_scatter_with_trend,
        yvar="meantime",
        yrange=[3*60,5.5*60],
        ytitle="Mean Finish Time (min)",
        height=230
    )
    return age_dist, age_timeseries, time_dist, time_timeseries

@app.callback(
    [
        Output('map','figure'),
        Output("geo-sunburst",'figure')
    ],
    [
        Input("by-geo-year-dropdown","value"), 
        Input("by-geo-gender-selector","value"), 
    ]
)
def update_data(years, genders):
    power = (3.5/12) 
    years = [yr for yr in range(years[0], years[1]+1)]
    plot_dt = data.filter_data(years, genders)
    plot_dt["freq_norm"] = plot_dt.freq**(power)
    fig_map = data.create_map(plot_dt)
    fig_sunburst = data.create_geo_sunburst(plot_dt)
    return fig_map, fig_sunburst


if __name__ == '__main__':
    app.run_server(debug=False,host="0.0.0.0",port=port)

