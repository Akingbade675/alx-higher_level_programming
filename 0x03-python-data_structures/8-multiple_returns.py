def multiple_returns(sentence):
    lent = len(sentence)
    return (lent, sentence[0] if lent else None)
