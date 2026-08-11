import streamlit as st

from engines.opportunity_engine import (

    best_region,

    best_category,

    highest_margin,

    weakest_category,

)


def render_opportunity(df):

    region = best_region(df)

    category = best_category(df)

    margin = highest_margin(df)

    weak = weakest_category(df)

    st.subheader("🚀 AI Opportunity Scanner")

    c1, c2 = st.columns(2)

    with c1:

        st.success(

            f"""
### 🌍 Best Region

**{region['Region']}**

Revenue

₦{region['Revenue']:,.2f}

Potential

₦{region['Potential']:,.2f}

Confidence

{region['Confidence']}%
"""
        )

    with c2:

        st.success(

            f"""
### 🛍 Best Category

**{category['Category']}**

Revenue

₦{category['Revenue']:,.2f}

Potential

₦{category['Potential']:,.2f}

Confidence

{category['Confidence']}%
"""
        )

    st.divider()

    c3, c4 = st.columns(2)

    with c3:

        st.info(

            f"""
### 💰 Highest Margin

{margin['Category']}

Margin

{margin['Margin']:.2f}%
"""
        )

    with c4:

        st.warning(

            f"""
### ⚠ Weakest Category

{weak['Category']}

Revenue

₦{weak['Revenue']:,.2f}

Recommendation

Increase promotion or review inventory.
"""
        )