from app import app
# import tabs.by_geography as by_geography
# import tabs.age as age
# import tabs.fast as fast
import tabs.intro as intro
# import tabs.slow as slow
import constants

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app.layout = html.Div(
    className='app-body', 
    children=[
        dcc.Tabs(
            id = "tabs",
            children=[
                intro.Layout().get(),
                # age.Layout().get(),
                # fast.Layout().get(),
                # slow.Layout().get(),
                # by_geography.layout(
                #     yearmin=constants.YEAR_RANGE[0], 
                #     yearmax=constants.YEAR_RANGE[1]
                # )
            ]
        )
    ]
)


# @app.callback(
#     [
#         Output('slow-whole-time-dist','figure'),
#         Output('slow-whole-time-timeseries','figure'),
#         Output('slow-proportion-by-race-timeseries','figure'),
#         Output('slow-number-slow-timeseries','figure')
#     ],
#     [
#         Input('slow-whole-time-gender-selector',"value"), 
#         Input("slow-whole-time-race-dropdown","value"), 
#         Input('slow-proportion-by-race-gender-selector',"value"), 
#         Input("slow-proportion-by-race-race-dropdown","value"), 
#         Input('slow-number-slow-gender-selector',"value"), 
#         Input("slow-number-slow-race-dropdown","value"), 
#     ]
# )
# def update_slow(gender, race, gender_prop, race_prop, gender_freq, race_freq):
#     prop_timeseries = age.create_fig(
#         slow.proportions_subset,
#         race_prop,
#         gender_prop,
#         fast.create_timeseries,
#         yvar = "prop_demeaned",
#         yrange = [-200,200],
#         ytitle = "Demeaned % Difference",
#     )
#     freq_timeseries = age.create_fig(
#         slow.number_slow,
#         race_freq,
#         gender_freq,
#         fast.create_timeseries,
#         yvar = "freq",
#         yrange = [
#             0,
#             slow.number_slow[(slow.number_slow.event_name == race_freq)].freq.max()
#         ],
#         ytitle = 'Number of "slow" Runners',
#     )
    
#     time_dist = age.create_fig(
#         slow.time_dist,
#         race, 
#         gender,
#         age.create_distribution,
#         xrange=[4,6.5],
#         yrange=[0,1]
#     )
#     time_timeseries = age.create_fig(
#         slow.time_mean,
#         race, 
#         gender,
#         age.create_timeseries,
#         yvar="finish_time",
#         yrange=[4.5*60,6.5*60],
#         ytitle="Mean Finish Time (min)"
#     )
#     return time_dist, time_timeseries, prop_timeseries, freq_timeseries

# @app.callback(
#     [
#         Output('fast-whole-time-dist','figure'),
#         Output('fast-whole-time-timeseries','figure'),
#         Output('fast-proportion-by-race-timeseries','figure'),
#         Output('fast-number-fast-timeseries','figure')
#     ],
#     [
#         Input('fast-whole-time-gender-selector',"value"), 
#         Input("fast-whole-time-race-dropdown","value"), 
#         Input('fast-proportion-by-race-gender-selector',"value"), 
#         Input("fast-proportion-by-race-race-dropdown","value"), 
#         Input('fast-number-fast-gender-selector',"value"), 
#         Input("fast-number-fast-race-dropdown","value"), 
#     ]
# )
# def update_fast(gender, race, gender_prop, race_prop, gender_freq, race_freq):
#     prop_timeseries = age.create_fig(
#         fast.proportions_subset,
#         race_prop,
#         gender_prop,
#         fast.create_timeseries,
#         yvar = "prop_demeaned",
#         yrange = [-200,200],
#         ytitle = "Demeaned % Difference",
#     )
#     freq_timeseries = age.create_fig(
#         fast.number_fast,
#         race_freq,
#         gender_freq,
#         fast.create_timeseries,
#         yvar = "freq",
#         yrange = [
#             0,
#             fast.number_fast[(fast.number_fast.event_name == race_freq)].freq.max()
#         ],
#         ytitle = 'Number of "strong" Amatuers',
#     )
    
#     time_dist = age.create_fig(
#         fast.time_dist,
#         race, 
#         gender,
#         age.create_distribution,
#         xrange=[2.45,3.1]
#     )
#     time_timeseries = age.create_fig(
#         fast.time_mean,
#         race, 
#         gender,
#         age.create_timeseries,
#         yvar="finish_time",
#         yrange=[2.25*60,3.25*60],
#         ytitle="Mean Finish Time (min)"
#     )
#     return time_dist, time_timeseries, prop_timeseries, freq_timeseries



# @app.callback(
#     [
#         Output('age-age-dist','figure'),
#         Output('age-age-timeseries','figure'),
#         Output('age-time-dist','figure'),
#         Output('age-time-timeseries','figure')
#     ],
#     [
#         Input('age-age-gender-selector',"value"), 
#         Input("age-age-race-dropdown","value"), 
#         Input('age-time-gender-selector',"value"), 
#         Input("age-time-race-dropdown","value"), 
#     ]
# )
# def update_age(age_gender, age_race, time_gender, time_race):
#     age_dist = age.create_fig(
#         age.age_dist,
#         age_race, 
#         age_gender,
#         age.create_distribution,
#         xrange = [15,86],
#         xtitle="Age"
#     )
#     age_timeseries = age.create_fig(
#         age.age_mean,
#         age_race, 
#         age_gender,
#         age.create_timeseries,
#         yvar="average_age",
#         ytitle="Mean Runner Age",
#         yrange=[30,55]
#     )
#     time_dist = age.create_fig(
#         age.time_dist,
#         time_race, 
#         time_gender,
#         age.create_distribution
#     )
#     time_timeseries = age.create_fig(
#         age.time_mean,
#         time_race, 
#         time_gender,
#         age.create_timeseries,
#         yvar="finish_time",
#         yrange=[3*60,5.5*60],
#         ytitle="Mean Finish Time (min)"
#     )
#     return age_dist, age_timeseries, time_dist, time_timeseries

# @app.callback(
#     [
#         Output('map','figure'),
#         Output("geo-sunburst",'figure')
#     ],
#     [
#         Input("by-geo-year-dropdown","value"), 
#         Input("by-geo-gender-selector","value"), 
#     ]
# )
# def update_by_geography(years, genders):
#     power = (3.5/12) 
#     years = [yr for yr in range(years[0], years[1]+1)]
#     plot_dt = by_geography.filter_data(years, genders)
#     plot_dt["freq_norm"] = plot_dt.freq**(power)
#     fig_map = by_geography.create_map(plot_dt)
#     fig_sunburst = by_geography.create_geo_sunburst(plot_dt)
#     return fig_map, fig_sunburst


if __name__ == '__main__':
    app.run_server(debug = True)
