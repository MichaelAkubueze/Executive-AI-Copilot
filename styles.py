from pathlib import Path
import streamlit as st


def load_css():

    assets = Path("assets")

    css = ""

    order = [
        "colors.css",
        "typography.css",
        "layout.css",
        "sidebar.css",
        "cards.css",
        "header.css",
        "charts.css",
        "animations.css",
    ]

    for name in order:

        path = assets / name

        if path.exists():
            css += path.read_text(encoding="utf-8") + "\n"

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True,
    )