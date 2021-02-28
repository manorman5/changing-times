import utils.timeseries as timeseries
import utils.utils as utils
import utils.layout as layout
import constants

import dash_core_components as dcc

import numpy as np
import pandas as pd

intro = """
##### Has an increasing number of "slow" marathoners caused the great slowing?

Over the past 25 years many marathon characteristics have changed. Marathons have grown 
in popularity, meaning the number of marathoners has dramatically grown. With this increase
in popularity, there has been an explosion of casual runners and the focus of runners has
generally shifted from running to win to running to participate. With this context in mind, its
easily imagineable that there are more "slow" runners relative to the number of racers 
today compared to 25 years ago. Below we will confirm this hypothesis and investigate the role of these
finishers in the great slowing.

For simplicity, we will continue to restrict our analysis to marathoners between
the ages of 25 and 35. This will ensure the observed trends are not attributable
to the aging marathoner population. Additionally, let's define a "slow"
marathoner as a runner who finishes between 4.5 and 6.5 hours. To begin, let's confirm the number of
"slow" runners has increased over the last 25 years.
"""

number_slow_description = number_fast_description = """
For all races and both genders, we see an increasing number of "slow"
runners through the years. Does that mean there are more "slow"
runners? Maybe, maybe not. If the trend we observe here is driven by the fastest
of the "slow" runners, I think we would all feel a bit more uneasy concluding that
the number of "slow" runners is increasing. To dig into this inquiry, let's look at
how the distribution of runners finishing between 4.5 and 6 hours has evolved over 
time and how the average finish time within this interval has changed. If "slow"
runners are getting slower I think we will more comfortable concluding
the number of "slow" runners has increased.
"""

slow_analysis = """
##### Are there really more "slow" runners?

For all races and both genders, we see the average slow runner got slower between 1995 and
2020. Similar to our analysis of the "strong" amatuers, I want to also analyze trends in the average percent
difference between histogram bars. Runners finishing in the first histogram bar 
(the one that contains 4.5 hr finishers) holds large sway in determining the 
average time for runners finishing between 4.5 and 6.5 hours. The first 
histogram bar contains 50 percent or more of the finishers. If we were to redesignate finishers within 
this subinterval as faster than "slow" runners, the trends we see in average finish time and number
of finishers for "slow" runners may change drastically. As with our analysis of the "strong"
amatuers, this isn't a game I want to play -- dropping histogram bars to see how the trend changes. 
Instead I want to change the approach. 

Really what we care about is how the number of finishers in one histogram bar relative to the previous has changed. If
all bars have an increasing number of finishers across time relative to the previous, then we can imagine there 
is an increasing number of "strong" amateur runners. Below, I conduct this analysis and find evidence 
that there is an increasing number of "slow" runners. The trendlines are positive, suggesting on average over
the entire distribution of "slow" runners there is an increasing number of slower runners. These findings
support the belief that there are more slower runners today than 25 years ago.
"""

prop_by_race_description = """
Each point represents the percent difference between the number of
finishers in two adjacent subintervals (histogram bars). Additionally, each point is demeaned, 
meaning the average percent difference between the number of finishers in two adjacent subintervals 
between 1995 and 2019 is subtracted from the percent difference in each year.
"""

prop_analysis = """
##### Are these results generalizable?

Now let's ensure there is evidence for all races that there is an increasing
number of "slow" runners. The trendlines below continue to support this conclusion. The slight 
positive trend below between time and adjacent subinterval percent differences suggest that on
average a races have seen an increasing number of "slow" runners. As above, each point represent the percent difference between
the number of finishers in two adjacent subintervals (histogram bars) for a given race. Additionally, 
each point is demeaned, meaning the average percent difference between the number of finisher in two adjacent
subintervals between 1995 and 2019 for a given race is subtracted from the percent difference in each year.

Given we find evidence to support the belief that there are more
"slow" runners today than 25 years ago, it is possible that this increase
in "slow" runners in the field is a driving cause of the great slowing. Below,
I will highlight the slowing trend is much greater for the "slow" runners
than for the other finishers.
"""

still_slowing = """
##### Which type of runner has slowed the most?

Both male and female "slow" runners have slowed over the past 25 years much more than "other" runners; 
other runers are defined as runners finishing between 2.5 and 4.5 hours. This finding supports the hypothesis
that an increase in slow runners is a driving cause of the great slowing of U.S. marathoners, at least
for the population of marathoners between 25 and 35 years.

An interesting next step could be to find the interval of finishers who experience the greatest slowing
over this time period. While my analysis finds "slow" runners to experience the greatest slowing over this
time period, I define fast and slow runners very arbitrarily throughout this analysis and do not check the
robustness of my findings to these arbitrary definitions. Using statistical analysis instead of arbitrary definitions
to find the interval of finishers who experience the greatest slowing could either support the findings here
or demonstrate the perrils of arbitrary definitions in data analytics. Hard telling not knowing. 
"""

prop_by_race_description = """
Each point represents the percent difference between the number of
finishers in two adjacent subintervals (histogram bars). Additionally, each point is demeaned, 
meaning the average percent difference between the number of finishers in two adjacent subintervals 
between 1995 and 2019 is subtracted from the percent difference in each year.
"""

finish_distribution_testages_slow = pd.read_csv(
    constants.DATA_DIR + "/" + utils.get_filename(
        typep="finishtime_distribution",
        contents="event_specific",
        modifier="",
        race_group="testages",
        speed="slow"
    )
)

finish_timeseries_testages_slow = pd.read_csv(
    constants.DATA_DIR + "/" + utils.get_filename(
        typep="finish_timeseries",
        contents="",
        modifier="demeaned_event",
        race_group="testages",
        speed="slow"
    )
)

finish_timeseries_testages_notslow = pd.read_csv(
    constants.DATA_DIR + "/" + utils.get_filename(
        typep="finish_timeseries",
        contents="",
        modifier="demeaned_event",
        race_group="testages",
        speed="notslow"
    )
)

proportion_timeseries_testages_slow = pd.read_csv(
    constants.DATA_DIR + "/" + utils.get_filename(
        typep="proportion_timeseries",
        contents="event_specific",
        modifier="demeaned_event",
        race_group="testages",
        speed="slow"
    )
)

runnerfreq_timeseries_testages_slow = pd.read_csv(
    constants.DATA_DIR + "/" + utils.get_filename(
        typep="runner_freq_timeseries",
        contents="event_specific",
        modifier="",
        race_group="testages",
        speed="slow"
    )
)


class Layout(layout.Layout):
    def get(self):
        return dcc.Tab(
            label='More "slow" Marathoners?',
            children=[
                self.row_description(intro),
                self.row_timeseries_by_race(
                    "slow", 
                    "number-slow", 
                    number_slow_description,
                    runnerfreq_timeseries_testages_slow.event_name.drop_duplicates().values
                ),
                self.row_dist_timeseries(
                    "slow",
                    "whole-time",
                    finish_distribution_testages_slow.event_name.drop_duplicates().values
                ),
                self.row_description(slow_analysis),
                self.row_timeseries_by_race(
                    "slow",
                    "proportion-by-race", 
                    prop_by_race_description,
                    proportion_timeseries_testages_slow.event_name.drop_duplicates().values
                ),
                self.row_description(prop_analysis),
                self.row_description(still_slowing),
                *[
                    self.row_side_by_side_graphs(
                        "slow", 
                        f"finish-timeseries-testages-notfast-{gender}", 
                        ["other","slow"],
                        timeseries.create_timeseries_by_ability,
                        df_dict = {
                            "other":finish_timeseries_testages_notslow[
                                finish_timeseries_testages_notslow.gender == gender[0]
                            ].copy(),
                            "slow":finish_timeseries_testages_slow[
                                finish_timeseries_testages_slow.gender == gender[0]
                            ].copy()
                        },
                        title = gender + " Runners",
                        color=constants.GENDER_COLORS[gender],
                        yrange=[-2*60,2*60], 
                        ytitle='Demeaned Mean Finish Time (min)',
                        yvar="meantime_demeaned"
                    )
                    for gender in ["Female","Male"]
                ]
            ]
        )