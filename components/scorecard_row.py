import streamlit as st


def scorecard_row(

    metric,

    actual,

    target,

    variance,

    achievement,

    status,

    trend,

):

    if achievement >= 100:

        colour="#10B981"

    elif achievement >=85:

        colour="#2563EB"

    elif achievement >=70:

        colour="#F59E0B"

    else:

        colour="#EF4444"

    st.markdown(

f"""

<div style="

padding:15px;

margin-bottom:12px;

border-radius:15px;

background:white;

box-shadow:0px 2px 8px rgba(0,0,0,.06);

">

<table width="100%">

<tr>

<td width="18%"><b>{metric}</b></td>

<td width="15%">Actual<br><b>{actual}</b></td>

<td width="15%">Target<br><b>{target}</b></td>

<td width="15%">Variance<br><b>{variance}</b></td>

<td width="15%">Achievement<br>

<b style="color:{colour};">{achievement:.1f}%</b>

</td>

<td width="12%">{status}</td>

<td width="10%">{trend}</td>

</tr>

</table>

</div>

""",

unsafe_allow_html=True,

)
    
    