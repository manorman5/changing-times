"""
Constants referencable from anywhere in app
"""

import plotly
import os 
import json

APP_ROOT = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = APP_ROOT + "/data"
LOCAL_DATA_DIR = "/data/marathon-data/int/marathon/changing_times" 

with open(APP_ROOT + "/assets/datafiles.json") as f:
    DATAFILES_CONFIG = json.load(f)

with open(APP_ROOT + "/assets/settings.json") as f:
    SETTINGS = json.load(f)

FIG_LAYOUT_DEFAULTS = dict(
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    xaxis={"showgrid":False},
    yaxis={"showgrid":False}
)

GENDER_COLORS = {
    "Female":'#333F44', 
    "Male":'#94F3E4', 
    "All":'#37AA9C'
}
GENDER_COLORS["M"] = GENDER_COLORS["Male"]
GENDER_COLORS["F"] = GENDER_COLORS["Female"]

REGION_COLORS = {
    "Midwest":plotly.colors.qualitative.D3[1], 
    "West":plotly.colors.qualitative.Pastel[3],
    "South":plotly.colors.qualitative.G10[5], 
    "Northeast":plotly.colors.qualitative.Plotly[2]
}

# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '20%',
    'padding': '20px 10px',
    'background-color': '#f8f9fa'
}

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '25%',
    'margin-right': '5%',
    'top': 0,
    'padding': '20px 10px'
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#191970'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}