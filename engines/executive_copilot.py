"""
Executive AI Copilot Interface

Simple wrapper around the Copilot Engine.
"""

from engines.copilot_engine import answer_question


class ExecutiveCopilot:

    def __init__(self, df):
        self.df = df

    def ask(self, question):
        return answer_question(self.df, question)