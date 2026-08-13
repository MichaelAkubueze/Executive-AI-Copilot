from engines.intent_library import INTENT_LIBRARY


def detect(question):

    q = question.lower()

    for intent, patterns in INTENT_LIBRARY.items():

        for phrase in patterns:

            if phrase in q:

                return intent

    return "unknown"