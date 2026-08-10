from pathlib import Path

import plotly.express as px


OUTPUT_FOLDER = Path("reports/generated_charts")
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)


def revenue_chart(df):

    monthly = (
        df.groupby("Month", as_index=False)["Revenue"]
        .sum()
    )

    fig = px.line(
        monthly,
        x="Month",
        y="Revenue",
        markers=True,
        title="Revenue Trend",
    )

    filename = OUTPUT_FOLDER / "revenue.png"

    fig.write_image(filename)

    return filename


def profit_chart(df):

    monthly = (
        df.groupby("Month", as_index=False)["Profit"]
        .sum()
    )

    fig = px.bar(
        monthly,
        x="Month",
        y="Profit",
        title="Profit Trend",
    )

    filename = OUTPUT_FOLDER / "profit.png"

    fig.write_image(filename)

    return filename