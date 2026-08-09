import streamlit as st
from datetime import datetime


def metric_card(
    title,
    value,
    icon="📊",
    trend="",
    target="",
    progress=0,
    badge="Healthy",
    badge_color="#10B981",
):

    now = datetime.now().strftime("%d %b %Y | %I:%M %p")

    if progress < 50:
        progress_color = "#EF4444"
    elif progress < 75:
        progress_color = "#F59E0B"
    else:
        progress_color = "#10B981"

    st.markdown(
        f"""
<div style="
background:white;
border:1px solid #E5E7EB;
border-radius:18px;
padding:20px;
box-shadow:0 6px 16px rgba(0,0,0,.08);
">

<div style="font-size:34px;">{icon}</div>

<div style="margin-top:10px;font-size:14px;color:#6B7280;">
{title}
</div>

<div style="margin-top:8px;font-size:30px;font-weight:700;color:#111827;">
{value}
</div>

<div style="margin-top:6px;font-size:14px;font-weight:600;color:#10B981;">
{trend}
</div>

<div style="margin-top:16px;background:#E5E7EB;height:8px;border-radius:8px;overflow:hidden;">
    <div style="width:{progress}%;background:{progress_color};height:8px;"></div>
</div>

<div style="margin-top:10px;font-size:13px;color:#6B7280;">
🎯 Target
<span style="float:right;font-weight:700;">{target}</span>
</div>

<div style="margin-top:16px;">
<span style="
background:{badge_color}20;
color:{badge_color};
padding:4px 12px;
border-radius:14px;
font-size:12px;
font-weight:700;
">
{badge}
</span>
</div>

<div style="margin-top:16px;font-size:11px;color:#9CA3AF;">
🕒 Updated {now}
</div>

</div>
""",
        unsafe_allow_html=True,
    )
    