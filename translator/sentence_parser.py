
import json

def parse_sentence(eva_tokens, lexicon):
    parsed = []
    for token in eva_tokens:
        if token in lexicon:
            word = {
                "eva": token,
                "meaning": lexicon[token]["meaning"],
                "pos": lexicon[token]["pos"]
            }
        else:
            word = {
                "eva": token,
                "meaning": "❓",
                "pos": "Unknown"
            }
        parsed.append(word)
    return parsed
