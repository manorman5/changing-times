import utils.layout as layout
import utils.timeseries as timeseries
import utils.utils as utils

import constants

import pandas as pd

import dash_core_components as dcc
import dash_html_components as html

finish_timeseries = pd.read_csv(constants.DATA_DIR + "/" + utils.get_filename(
    typep="finish_timeseries",
    contents="",
    modifier="demeaned_event",
    race_group="",
    speed=""
))

intro_description = """
#### The Trend and The Hypotheses
As elite marathoners continue to break records, non-elite marathoners are slowing on average. The average female and male marathoner is 
slower today than they were 25 years ago. Although this trend's cause is unknown, many running aficianados have floated hypotheses attempting to 
explain this trend. There are fewer strong amateurs in the field. Generally marathoners' focus has shifted from running to win to running to
participate. Marathoners today are on average older than marathoners 20 years ago. The increase in marathon popularity disproportionatley increased
the number of slower marathoners. After accumlating a rather extensive set of U.S. marathon results, I decided to run with these
hypotheses and see what the data had to say. 

To begin, let's confirm we aren't hunting a ghost and the slowing trend documented throughout 
the internet exists in this dataset. Below, I highlight on average non-elite marathoners are slower today than they were 25 years ago.
The trendlines below highlight that the average male and female marathoner has slowed over the last 25 years. Each point represents the demeaned mean finish time for a given race in a given year. Where the demeaned mean finish time is the mean finish
time for a given race in a given year minus the mean finish time for a given race in all years. Additionally, the lines are OLS trendlines through the
demeaned mean finish times.
"""

class Layout(layout.Layout):
    def get(self):
        return dcc.Tab(
            label="The Average Marathoner is Slowing -- Why?",
            children=[
                self.row_description(intro_description),
                self.row_side_by_side_graphs(
                    "intro", 
                    "finish-timeseries", 
                    ["Female","Male"],
                    timeseries.create_timeseries_by_gender,
                    df = finish_timeseries,
                    yrange=[-2*60,2*60], 
                    ytitle='Demeaned Mean Finish Time (min)',
                    yvar="meantime_demeaned"
                )
            ]
        )