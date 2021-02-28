import constants

import dash_core_components as dcc
import dash_html_components as html

class Layout: 
    def row_side_by_side_graphs(self, ptag, gtag, glist, figurefunc, **kwargs):
        return html.Div(
            className="row", 
            children=[ 
                html.Div(
                    className="six columns pretty_container", 
                    children=[
                        dcc.Graph(
                            id=f'{ptag}-{gg}-{gtag}',
                            figure=figurefunc(
                                gg,
                                **kwargs
                            )
                        )
                    ],
                )
                for gg in glist
            ]
        )
    def row_timeseries_by_race(self, ptag, gtag, description, eventnames):
        return html.Div(
            className="row", 
            children=[
                html.Div(
                    className="seven columns pretty_container", 
                    children=[
                        dcc.Graph(id=f'{ptag}-{gtag}-timeseries')
                    ],
                ),
                html.Div(
                    className="five columns pretty_container", 
                    children=[
                        dcc.Markdown(children=description),
                        html.Hr(),
                        html.P('Select a gender', className="control_label"),
                        dcc.Dropdown(
                            id=f'{ptag}-{gtag}-gender-selector',
                            options=[
                                {'label': 'Male', 'value': "M"},
                                {'label': 'Female', 'value': "F"},
                            ],
                            value="M",
                        ),
                        html.P("Select a race", className="control_label"),
                        dcc.Dropdown(
                            id=f"{ptag}-{gtag}-race-dropdown",
                            value=eventnames[0],
                            options=[
                                {"value":event_name, "label":event_name}
                                for event_name in eventnames
                            ]
                        ),
                    ]
                ),
            ]
        )
    def row_dist_timeseries(self, ptag, gtag, eventnames):
        return html.Div(
            className="row", 
            children=[
                html.Div(
                    className="seven columns pretty_container", 
                    children=[
                        dcc.Graph(id=f'{ptag}-{gtag}-dist')
                    ],
                ),
                html.Div(
                    className="five columns pretty_container", 
                    children=[
                        dcc.Graph(id=f'{ptag}-{gtag}-timeseries'),
                        html.Hr(),
                        html.P('Select a gender', className="control_label"),
                        dcc.Dropdown(
                            id=f'{ptag}-{gtag}-gender-selector',
                            options=[
                                {'label': 'Male', 'value': "M"},
                                {'label': 'Female', 'value': "F"},
                            ],
                            value="M",
                        ),
                        html.P("Select a race", className="control_label"),
                        dcc.Dropdown(
                            id=f"{ptag}-{gtag}-race-dropdown",
                            value=eventnames[0],
                            options=[
                                {"value":event_name, "label":event_name}
                                for event_name in eventnames
                            ]
                        )
                    ]
                ),
            ]
        )
    def row_description(self, description):
        return html.Div(
            className="row",
            children=[
                html.Hr(),
                html.Div(
                    className="twelve columns pretty_container",
                    children=[dcc.Markdown(children=description)]
                )
            ]
        )