import constants
import utils.utils as utils
import utils.timeseries as timeseries
import utils.layout as layout

import pandas as pd

import dash_core_components as dcc

aging_intro = """
##### Is an aging marathon population causing the great slowing? 
If so, we first need to confirm the marathon population is aging. I do so for a handful of marathons below.
We can see for these marathons, both the female and male marathoner populations are aging. As you move from the
past to the present, the marathoner age distribution moves to the right, indicating the population is aging. 
Additionally, the trendline in mean runner age has a positive slope indicating the average marathoner age 
has increased over the last 25 years. 
"""

aging_analysis = """
##### Are 25-35 year old marathoners slowing?
Great, the marathoner population is aging... is that why the average marathoner is slower today than 25 years ago? Maybe... 
maybe not. Hard telling not knowing. To partially test this question, let's see if 25-35 year old marathoners
today are slower on average than 30 year old marathoners 25 years ago. If the slowing trend holds for 25-35 year
old runners, the aging marathoner population is not fully responsible for the great slowing under investigation. Below, 
I demonstrate that generally 25-35 year old marathoners have slowed over the past 25 years. The finish time
distribution of these marathoners has shifted right and the distribution spread has increased. The trendline in mean finish
time has a positive slope indicating the average marathoner has slowed.
"""

generalizable_conclusions = """
##### Are these conclusions generalizable?

Now, let's ensure our finding that the average 25-35 year old marathoner is slower today than 25 years ago applies to all races 
in the dataset. The trendlines below highlight that the average 25-35 year old marathoner across all races has in fact slowed over the past 25 years.
Each point represents the demeaned mean finish time for 25-35 year old racers for a given race in a given year. Where the demeaned 
mean finish time is the mean finish time for a given race in a given year minus the mean finish time for a given race in all years. 
Additionally, the lines are OLS trendlines through the demeaned mean finish times. 
"""

finish_distribution_testages = pd.read_csv(
    constants.DATA_DIR + "/" + utils.get_filename(
        typep="finishtime_distribution",
        contents="event_specific",
        modifier="",
        race_group="testages",
        speed=""
    )
)

age_distribution = pd.read_csv(
    constants.DATA_DIR + "/" + utils.get_filename(
        typep="age_distribution",
        contents="event_specific",
        modifier="",
        race_group="",
        speed=""
    )
)

age_timeseries = pd.read_csv(
    constants.DATA_DIR + "/" + utils.get_filename(
        typep="age_timeseries",
        contents="event_specific",
        modifier="",
        race_group="",
        speed=""
    )
)

finish_timeseries_testages = pd.read_csv(
    constants.DATA_DIR + "/" + utils.get_filename(
        typep="finish_timeseries",
        contents="",
        modifier="demeaned_event",
        race_group="testages",
        speed=""
    )
)

class Layout(layout.Layout):
    def get(self):
        return dcc.Tab(
            label="Aging marathoners?",
            children=[
                self.row_description(aging_intro),
                self.row_dist_timeseries(
                    "age",
                    "age", 
                    eventnames=age_distribution.event_name.drop_duplicates().values
                ),
                self.row_description(aging_analysis),
                self.row_dist_timeseries(
                    "age",
                    "time",
                    eventnames=finish_distribution_testages.event_name.drop_duplicates().values
                ),
                self.row_description(generalizable_conclusions),
                self.row_side_by_side_graphs(
                    "age", 
                    "finish-timeseries-testages", 
                    ["Female","Male"],
                    timeseries.create_timeseries_by_gender,
                    df = finish_timeseries_testages,
                    yrange=[-2*60,2*60], 
                    ytitle='Demeaned Mean Finish Time (min)',
                    yvar="meantime_demeaned"
                )
            ]
        )