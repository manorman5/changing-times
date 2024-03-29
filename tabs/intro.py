"""
Intro tab contents:
    * data
    * writing
    * layoung
"""

import utils.layout as layout
import utils.timeseries as timeseries
import utils.utils as utils

import constants

import pandas as pd

import dash_core_components as dcc
import dash_html_components as html

# average finish time time series by gender for all runners demeaned by event
finish_timeseries = pd.read_csv(constants.DATA_DIR + "/" + utils.get_filename(
    typep="finish_timeseries",
    contents="",
    modifier="demeaned_event",
    race_group="",
    speed=""
))

intro_description = """
##### The Trend and The Hypotheses
As elite marathoners continue to break records, non-elite marathoners are slowing. The average female and male marathoner is 
slower today than they were 25 years ago. Although this trend's cause is unknown, many running aficianados have floated hypotheses attempting to 
explain this trend. Below are a few: 
* There are fewer strong amateurs in the field. 
* Generally marathoners' focus has shifted from running to win to running to
participate. 
* Marathoners today are on average older than marathoners 20 years ago. 
* The increase in marathon popularity disproportionatley increased
the number of slower marathoners. 

After accumlating a rather extensive set of U.S. marathon results, I decided to run with these
hypotheses and see what the data had to say. To begin, let's confirm we aren't hunting a ghost and the slowing trend documented throughout 
the internet exists in this dataset. The trendlines below highlight on average non-elite marathoners are slower today than they were 25 years ago.
I define non-elite marathoners as marathoners that finish a marathon between 2.5 and 6.5 hours. Each point represents the demeaned mean 
finish time for a given race in a given year. Where the demeaned mean finish time is the mean finish time for a given race in a given year minus the mean finish 
time for a given race in all years.

Now, let's explore why the average marathoner today is slower than the average marathoner 25 years ago :).
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
                    yvar="meantime_demeaned",
                    hovertext=True,
                    marker_opacity=0.25
                )
            ]
        )
