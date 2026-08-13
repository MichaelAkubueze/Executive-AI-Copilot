import streamlit as st

from engines.risk_engine import (

    revenue_risk,

    margin_risk,

    customer_risk,

    category_risk,

)


def render_risk(df):

    rev = revenue_risk(df)

    margin = margin_risk(df)

    customer = customer_risk(df)

    weak = category_risk(df)

    st.subheader("🚨 AI Risk Radar")

    c1, c2 = st.columns(2)

    with c1:

        st.error(

            f"""
### Revenue Risk

{rev[0]}

Achievement

{rev[1]:.1%}
"""
        )

        st.warning(

            f"""
### Margin Risk

{margin[0]}

Margin

{margin[1]:.2f}%
"""
        )

    with c2:

        st.warning(

            f"""
### Customer Concentration

{customer[0]}

Largest Customer

{customer[1]:.1%}
"""
        )

        st.info(
    f"""
### ⚠ Weakest Category

**Category**

{weak["Category"]}

**Revenue**

₦{weak["Revenue"]:,.2f}

**Risk**

{weak["Risk"]}

**Recommendation**

Review immediately.
"""
)