#!/usr/bin/python3
def multiple_returns(sentence):
    length_sentence = len(sentence)

    if sentence is None or length_sentence == 0:
        return 0, None

    return length_sentence, sentence[0]
