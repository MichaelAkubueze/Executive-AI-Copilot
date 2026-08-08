import streamlit as st


def load_css():
    st.markdown("""
<style>

/* ===========================================================
GLOBAL
=========================================================== */

html,
body,
[class*="css"] {
    font-family: "Segoe UI", Arial, Helvetica, sans-serif;
    color: #0F172A;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

.stApp{
    background:#F4F7FB;
}


/* ===========================================================
SIDEBAR
=========================================================== */

[data-testid="stSidebar"]{
    background:#0F172A;
    border-right:1px solid #1E293B;
}

[data-testid="stSidebar"] *{
    color:white !important;
}

[data-testid="stSidebar"] hr{
    border-color:#334155;
}


/* ===========================================================
HEADERS
=========================================================== */

h1{
    color:#0F172A !important;
    font-size:40px !important;
    font-weight:800 !important;
    margin-bottom:0.25rem !important;
    text-shadow:none !important;
    filter:none !important;
    opacity:1 !important;
}

h2{
    color:#1E293B !important;
    font-size:28px !important;
    font-weight:700 !important;
    text-shadow:none !important;
}

h3{
    color:#334155 !important;
    font-size:22px !important;
    font-weight:600 !important;
}


/* ===========================================================
TEXT
=========================================================== */

p,
span,
small,
label,
div{
    text-shadow:none !important;
    filter:none !important;
    opacity:1 !important;
}


/* ===========================================================
CAPTIONS
=========================================================== */

[data-testid="stCaptionContainer"]{

    color:#64748B !important;

    font-size:16px !important;

    font-weight:500 !important;

}


/* ===========================================================
KPI METRICS
=========================================================== */

[data-testid="metric-container"]{

    background:white;

    border-radius:18px;

    padding:20px;

    border:1px solid #E5E7EB;

    box-shadow:0 6px 16px rgba(0,0,0,.08);

}

[data-testid="metric-container"] label{

    color:#64748B !important;

    font-size:14px !important;

    font-weight:600 !important;

}

[data-testid="metric-container"] [data-testid="stMetricValue"]{

    color:#0F172A !important;

    font-size:30px !important;

    font-weight:800 !important;

}


/* ===========================================================
CHART CONTAINERS
=========================================================== */

.js-plotly-plot{

    background:white;

    border-radius:18px;

    padding:10px;

    box-shadow:0 6px 16px rgba(0,0,0,.08);

}


/* ===========================================================
BUTTONS
=========================================================== */

.stButton>button{

    background:#2563EB;

    color:white;

    border:none;

    border-radius:10px;

    font-weight:600;

    padding:10px 20px;

}

.stButton>button:hover{

    background:#1D4ED8;

}


/* ===========================================================
SELECT BOXES
=========================================================== */

.stSelectbox{

    background:white;

}


/* ===========================================================
DATAFRAMES
=========================================================== */

[data-testid="stDataFrame"]{

    border-radius:18px;

    overflow:hidden;

}


/* ===========================================================
SUCCESS / INFO
=========================================================== */

.stSuccess,
.stInfo,
.stWarning,
.stError{

    border-radius:14px;

}


/* ===========================================================
DIVIDERS
=========================================================== */

hr{

    border:0;

    border-top:1px solid #E5E7EB;

}


/* ===========================================================
HIDE STREAMLIT BRANDING
=========================================================== */

#MainMenu{

    visibility:hidden;

}

footer{

    visibility:hidden;

}

header{

    visibility:hidden;

}

</style>
""", unsafe_allow_html=True)