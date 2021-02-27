import constants

def get_filename(typep, contents, modifier,race_group, speed):
    def parameter_test(param, paramtype):
        options = constants.DATAFILES_CONFIG[paramtype]
        options_str = options.join(", ")
        assert param is in constants.DATAFILES_CONFIG[paramtype], f"`{paramtype}` parameter is invalid. {param} is not in {options_str}"
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
        
    return f"{contents}{modifier}{typep}{age_group}{speed}.csv"


