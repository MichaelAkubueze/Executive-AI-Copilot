import plotly.graph_objects as go


#def executive_gauge(title, value, target, color="#2563EB"):
def executive_gauge(
    title,
    actual,
    target,
    colour="#2563EB",
):
    achievement = 0

    if target > 0:
        #achievement = value / target * 100
        achievement = actual / target * 100

    achievement = min(achievement, 100)

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",

            value=achievement,

            number={
                "suffix": "%",
                "font": {"size": 36}
            },

            title={
                "text": f"<b>{title}</b>",
                "font": {"size": 18}
            },

            gauge={

                "axis": {
                    "range": [0, 100],
                    "tickwidth": 1,
                    "tickcolor": "#CBD5E1"
                },

                "bar": {
                    #"color": color,
                    "color": colour,
                    "thickness": 0.35
                },

                "bgcolor": "#F8FAFC",

                "borderwidth": 0,

                "steps": [

                    {
                        "range": [0, 50],
                        "color": "#FEE2E2"
                    },

                    {
                        "range": [50, 75],
                        "color": "#FEF3C7"
                    },

                    {
                        "range": [75, 100],
                        "color": "#DCFCE7"
                    }

                ],

                "threshold": {

                    "line": {
                        "color": "#111827",
                        "width": 5
                    },

                    "value": achievement

                }

            }

        )
    )

    fig.update_layout(

        height=320,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        paper_bgcolor="white",

        plot_bgcolor="white",

        font=dict(
            family="Segoe UI"
        )

    )

    return fig