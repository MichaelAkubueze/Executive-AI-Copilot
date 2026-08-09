from intent_engine import detect_intent

from kpi import (
    get_total_revenue,
    get_total_profit,
    get_total_customers,
    get_total_orders,
    get_gross_margin,
)

from analytics import (
    get_sales_by_region,
    get_sales_by_category,
)

from advisor import generate_recommendation


class ExecutiveCopilot:

    def __init__(self, df):
        self.df = df

    def ask(self, question):

        intent = detect_intent(question)

        # --------------------------------------------------
        # Revenue
        # --------------------------------------------------

        if intent == "revenue":

            return (
                f"💰 Total Revenue\n\n"
                f"₦{get_total_revenue(self.df):,.2f}"
            )

        # --------------------------------------------------
        # Profit
        # --------------------------------------------------

        elif intent == "profit":

            return (
                f"📈 Total Profit\n\n"
                f"₦{get_total_profit(self.df):,.2f}"
            )

        # --------------------------------------------------
        # Gross Margin
        # --------------------------------------------------

        elif intent == "margin":

            return (
                f"📊 Gross Margin\n\n"
                f"{get_gross_margin(self.df):.2%}"
            )

        # --------------------------------------------------
        # Orders
        # --------------------------------------------------

        elif intent == "orders":

            return (
                f"🛒 Total Orders\n\n"
                f"{get_total_orders(self.df):,}"
            )

        # --------------------------------------------------
        # Customers
        # --------------------------------------------------

        elif intent == "customers":

            return (
                f"👥 Total Customers\n\n"
                f"{get_total_customers(self.df):,}"
            )

        # --------------------------------------------------
        # Best Region
        # --------------------------------------------------

        elif intent == "best_region":

            region = get_sales_by_region(self.df).iloc[0]

            return (
                f"🏆 Best Performing Region\n\n"
                f"Region : {region['Region']}\n"
                f"Revenue : ₦{region['Revenue']:,.2f}"
            )

        # --------------------------------------------------
        # Worst Region
        # --------------------------------------------------

        elif intent == "worst_region":

            region = get_sales_by_region(self.df).iloc[-1]

            return (
                f"⚠️ Lowest Performing Region\n\n"
                f"Region : {region['Region']}\n"
                f"Revenue : ₦{region['Revenue']:,.2f}"
            )

        # --------------------------------------------------
        # Best Category
        # --------------------------------------------------

        elif intent == "best_category":

            category = get_sales_by_category(self.df).iloc[0]

            return (
                f"🥇 Best Product Category\n\n"
                f"Category : {category['Category']}\n"
                f"Revenue : ₦{category['Revenue']:,.2f}"
            )

        # --------------------------------------------------
        # Recommendation
        # --------------------------------------------------

        elif intent == "recommendation":

            return generate_recommendation(self.df)

        # --------------------------------------------------
        # Unknown Question
        # --------------------------------------------------

        else:

            return (
                "🤖 I couldn't understand your question.\n\n"
                "Try asking:\n\n"
                "• Revenue\n"
                "• Profit\n"
                "• Gross Margin\n"
                "• Orders\n"
                "• Customers\n"
                "• Best Region\n"
                "• Worst Region\n"
                "• Best Category\n"
                "• Recommendation\n\n"
                "You can also ask naturally, for example:\n"
                "• How much money did we make?\n"
                "• Which region performed best?\n"
                "• What is our profit?\n"
                "• Show the best product category."
            )