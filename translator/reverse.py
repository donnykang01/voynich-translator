
import json

LEXICON_PATH = "voynich_lexicon_expanded.json"

def load_lexicon(path=LEXICON_PATH):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def reverse_lookup(english_word, lexicon):
    for token, entry in lexicon.items():
        if isinstance(entry, dict) and entry.get("meaning") == english_word:
            return token
    return None
