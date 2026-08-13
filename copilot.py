"""
==========================================================
Executive AI Configuration

Central configuration values for Executive AI.
Changing values here affects the entire application.

Version : 6.0 RC1
==========================================================
"""
from engines.copilot_engine import answer_question

class ExecutiveCopilot:

    def __init__(self, df):
        self.df = df

    def ask(self, question):
        return answer_question(self.df, question)