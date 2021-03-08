"""
`Fewer "strong" amatuers?` contents:
    * writing
    * data
    * layout
"""
 
import utils.utils as utils
import utils.layout as layout
import utils.timeseries as timeseries

import constants

import dash_core_components as dcc

import numpy as np
import pandas as pd


##################################################################################################
# Tab writing - analysis and description
##################################################################################################

intro = """
##### Has a decreasing number of "strong" amateur runners caused the great slowing?

Over the past 25 years many marathon characteristics have changed. Marathons have grown 
in popularity, meaning the number of marathoners has dramatically grown. With this increase
in popularity, there has been an explosion of casual runners and the focus of runners has
generally shifted from running to win to running to participate. With this context in mind, its
easily imagineable that there are fewer "strong" amateur runners relative to the number of racers 
today compared to 25 years ago. Here, we are asking a different question though. Holding the number
of racers and the composition of not "strong" amateur runners constant, are there fewer "strong"
amateurs today than 25 years ago?

For simplicity, we will continue to restrict our analysis to marathoners between
the ages of 25 and 35. This will ensure the observed trends are not attributable
to the aging marathoner population. Additionally, let's define a "strong"
amateur as a runner who finishes between 2.5 and 3 hours. To begin, let's confirm the number of
"strong" amatuer runners has decreased over the last 25 years.
"""

number_fast_description = """
For all races and both genders, we see an increasing number of "strong" amatuer
runners through the years. Does that mean there are more "strong" amatuer
runners? Maybe, maybe not. If the trend we observe here is driven by the slowest
of the "strong" amatuers, I think we would all feel a bit more uneasy concluding that
the number of "strong" amatuers is increasing. To dig into this inquiry, let's look at
how the distribution of runners finishing between 2.5 and 3 hours has evolved over 
time and how the average finish time within this interval has changed. If "strong"
amatuers are getting slower I think we will feel less comfortable concluding
the number of "strong" amatuers has increased.
"""

fast_analysis = """
##### Are there really fewer "strong" amateurs?

The obvious conclusion here is there is no obvious conclusion. For the Chicago Marathon,
both "strong" male and female amateur runners marginally slowed over this time period. For Grandma's marathon,
both "strong" male and female amateur runners marginally sped up over this time period. In the Houston marathon,
average finish times for both "strong" male and female amateurs barely changed over the time period.

More importantly though, I want to draw your attention to a pitfall of the approach I've taken above.
Runners finishing in the final histogram bar (the one that contains 3 hr finishers) holds large sway
in determining all summary statisitcs about runners finishing between 2.5 and 3 hours. The final 
histogram bar contains 20-40 percent of the finishers. If we were to redesignate finishers within 
this subinterval as sub "strong" amateur runners, the trends we see in average finish time and the number of finishers 
may change drastically. This isn't a game I want to play though -- dropping histogram bars
to see how the trend changes. Instead I want to change the approach. 

Really what we care about is how the number of finishers in one histogram bar relative to the previous has changed. If
all bars have an increasing number of finishers across time relative to the previous, then we can imagine there is a decreasing
number of "strong" amateur runners. Below, I conduct this analysis and find little if any evidence that
there is a decreasing number of "strong" amateur runners. The trend lines are weak at best, and evidence of a linear
relationship between time and changes in the percent difference between adjacent subintervals is weak. 
"""

prop_by_race_description = """
Each point represents the percent difference between the number of
finishers in two adjacent subintervals (histogram bars). Additionally, each point is demeaned, 
meaning the average percent difference between the number of finishers in two adjacent subintervals 
between 1995 and 2019 is subtracted from the percent difference in each year.
"""

prop_analysis = """
##### What do these results (or lack there of) mean?

Given we do not find evidence to support the belief that there are fewer
"strong" amatuers today than 25 years ago for our sample races, 
it is unlikely that a reduction in "strong" amatuers in the field is 
a driving cause of the great slowing. 

To satiate the curiousity of the most curious or the most skeptical, 
I'll demonstrate below that the slowing trend persists after dropping 
all runners we've defined as "strong" amatuers from the sample.
"""

still_slowing = """
##### If we drop the "strong" amatuers is the average marathoner still slowing?

Both male and female sub "strong" amatuers have slowed over the past 25 years much more than "strong" amatuers; 
other runers are defined as runners finishing between 3 and 6.5 hours. This finding does not support the hypothesis
that a decrease in fast runners is a driving cause of the great slowing of U.S. marathoners, at least
for the population of marathoners between 25 and 35 years.
"""

#################################################################################
# Tab data
#################################################################################

# finish time distribution for 25-35 year olds who finished faster than 2.5 hours
finish_distribution_testages_fast = pd.read_csv(
    constants.DATA_DIR + "/" + utils.get_filename(
        typep="finishtime_distribution",
        contents="event_specific",
        modifier="",
        race_group="testages",
        speed="fast"
    )
)

# finish time average time series for 25-35 year olds who finished faster than 2.5 hours
finish_timeseries_testages_fast = pd.read_csv(
    constants.DATA_DIR + "/" + utils.get_filename(
        typep="finish_timeseries",
        contents="",
        modifier="demeaned_event",
        race_group="testages",
        speed="fast"
    )
)

# finish time average time series for 25-35 year olds who finished slower than 3 hours
finish_timeseries_testages_notfast = pd.read_csv(
    constants.DATA_DIR + "/" + utils.get_filename(
        typep="finish_timeseries",
        contents="",
        modifier="demeaned_event",
        race_group="testages",
        speed="notfast"
    )
)

# percent differences between adjacent number of finishers in adjacent bins 
# for 25-35 year olds who finished faster than 2.5 hours
proportion_timeseries_testages_fast = pd.read_csv(
    constants.DATA_DIR + "/" + utils.get_filename(
        typep="proportion_timeseries",
        contents="event_specific",
        modifier="demeaned_event",
        race_group="testages",
        speed="fast"
    )
)

# number of finishers for 25-35 year olds who finished faster than 2.5 hours 
runnerfreq_timeseries_testages_fast = pd.read_csv(
    constants.DATA_DIR + "/" + utils.get_filename(
        typep="runner_freq_timeseries",
        contents="event_specific",
        modifier="",
        race_group="testages",
        speed="fast"
    )
)

#################################################################################
# Tab layout
#################################################################################

class Layout(layout.Layout):
    def get(self):
        return dcc.Tab(
            label='Fewer "strong" Amateurs?',
            children=[
                self.row_description(intro),
                self.row_timeseries_by_race(
                    "fast", 
                    "number-fast", 
                    number_fast_description, 
                    runnerfreq_timeseries_testages_fast.event_name.drop_duplicates().values
                ),
                self.row_dist_timeseries(
                    "fast",
                    "whole-time",
                    finish_distribution_testages_fast.event_name.drop_duplicates().values
                ),
                self.row_description(fast_analysis),
                self.row_timeseries_by_race(
                    "fast",
                    "proportion-by-race", 
                    prop_by_race_description,
                    proportion_timeseries_testages_fast.event_name.drop_duplicates().values
                ),
                self.row_description(prop_analysis),
                self.row_description(still_slowing),
                *[
                    self.row_side_by_side_graphs(
                        "fast", 
                        f"finish-timeseries-testages-{gender}", 
                        ["other","fast"],
                        timeseries.create_timeseries_by_ability,
                        df_dict = {
                            "other":finish_timeseries_testages_notfast[
                                finish_timeseries_testages_notfast.gender == gender[0]
                            ].copy(),
                            "fast":finish_timeseries_testages_fast[
                                finish_timeseries_testages_fast.gender == gender[0]
                            ].copy()
                        },
                        title = gender + " Runners",
                        color=constants.GENDER_COLORS[gender],
                        yrange=[-2*60,2*60], 
                        ytitle='Demeaned Mean Finish Time (min)',
                        yvar="meantime_demeaned",
                        hovertext=True,
                        marker_opacity=0.25
                    )
                    for gender in ["Female","Male"]
                ]
            ]
        )
