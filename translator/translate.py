
import json
import re

LEXICON_PATH = "voynich_lexicon_expanded.json"
PUNCTUATION = re.compile(r'[.!,-]')

def load_lexicon(path=LEXICON_PATH):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def tokenize(eva_line):
    return [PUNCTUATION.sub("", t) for t in eva_line.strip().split()]

def translate(tokens, lexicon):
    result = []
    for token in tokens:
        entry = lexicon.get(token)
        if isinstance(entry, dict):
            result.append((token, entry.get("pos", "Unknown"), entry.get("meaning", "")))
        else:
            result.append((token, "Unknown", f"❓ {token}"))
    return result

def process_line(eva_line, lexicon):
    tokens = tokenize(eva_line)
    return translate(tokens, lexicon)
