import streamlit as st


def load_css():

    st.markdown("""
<style>

/* ==========================================
BACKGROUND
========================================== */

.stApp{
    background:#F5F7FB;
}


/* ==========================================
MAIN CONTENT
========================================== */

.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
    padding-left:2rem;
    padding-right:2rem;
}


/* ==========================================
HEADINGS
========================================== */

h1{
    color:#0F172A;
    font-weight:700;
}

h2{
    color:#1E293B;
}

h3{
    color:#334155;
}


/* ==========================================
METRIC CARDS
========================================== */

[data-testid="stMetric"]{

    background:white;

    border-radius:18px;

    padding:18px;

    border:1px solid #E5E7EB;

    box-shadow:0 3px 10px rgba(0,0,0,.06);

}


/* ==========================================
BUTTONS
========================================== */

.stButton>button{

    width:100%;

    border-radius:10px;

    border:none;

    background:#2563EB;

    color:white;

    font-weight:600;

    height:42px;

}

.stButton>button:hover{

    background:#1D4ED8;

}


/* ==========================================
SIDEBAR
========================================== */

section[data-testid="stSidebar"]{

    background:white;

}


/* ==========================================
TEXT INPUT
========================================== */

.stTextInput input{

    border-radius:12px;

}


/* ==========================================
EXPANDERS
========================================== */

.streamlit-expanderHeader{

    font-weight:600;

}


/* ==========================================
SUCCESS
========================================== */

.stAlert{

    border-radius:12px;

}


/* ==========================================
CHART CONTAINERS
========================================== */

div[data-testid="stPlotlyChart"]{

    background:white;

    border-radius:18px;

    padding:15px;

    border:1px solid #ECECEC;

    box-shadow:0 2px 10px rgba(0,0,0,.05);

}

</style>
""", unsafe_allow_html=True)