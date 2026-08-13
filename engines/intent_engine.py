from engines.intent_library import INTENT_LIBRARY


def detect_intent(question):

    if not question:
        return "unknown"

    q = question.lower().strip()

    matches = []

    for intent, phrases in INTENT_LIBRARY.items():
        for phrase in phrases:
            if phrase.lower() in q:
                matches.append((len(phrase), intent))

    if matches:
        # Return the intent with the longest matching phrase
        matches.sort(reverse=True)
        return matches[0][1]

    return "unknown"
