import constants

def get_filename(typep, contents, modifier,race_group, speed):
    def parameter_test(param, paramtype):
        options = constants.DATAFILES_CONFIG[paramtype]
        options_str = ", ".join(options)
        assert param in constants.DATAFILES_CONFIG[paramtype], f"`{paramtype}` parameter is invalid. {param} is not in {options_str}"
    parameter_test(typep, "type"),
    parameter_test(contents, "contents")
    parameter_test(modifier, "modifier")
    parameter_test(race_group, "race_group")
    parameter_test(speed, "speed")
    
    if speed:
        speed = f"-{speed}"
    if race_group:
        race_group = f"-{race_group}"
    if modifier:
        modifier = f"{modifier}_"
    if contents:
        contents = f"{contents}_"

    return f"{contents}{modifier}{typep}{race_group}{speed}.csv"

def create_fig_by_gender_and_by_race(df, race, gender, figgen, **kwargs):
    if (not race) or (not gender):
        fig = go.Figure(data=[], layout={}, frames=[])
        fig.update_layout(**constants.FIG_LAYOUT_DEFAULTS)
        return fig
    df = df[
        (df.event_name == race)
        & (df.gender == gender)
    ].copy()
    color = constants.GENDER_COLORS[gender]
    return figgen(df, color, **kwargs)

def frame_args(duration):
    return {
        "frame": {"duration": duration, "redraw": True},
        "mode": "immediate",
        "fromcurrent": True,
        "transition": {"duration": duration, "easing": "linear"},
    }