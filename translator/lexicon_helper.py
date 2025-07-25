
import json

# Simple suffix and prefix-based rules for gloss suggestion
MORPHO_RULES = {
    "prefix": {
        "qo": "action",
        "ok": "sense",
        "lo": "light",
        "ro": "rotate",
    },
    "suffix": {
        "dy": "flow",
        "aiin": "cycle",
        "edy": "open",
        "or": "vision",
        "ain": "pattern"
    }
}

def suggest_gloss(word):
    prefix = next((p for p in MORPHO_RULES["prefix"] if word.startswith(p)), None)
    suffix = next((s for s in MORPHO_RULES["suffix"] if word.endswith(s)), None)
    if prefix or suffix:
        guess = []
        if prefix:
            guess.append(MORPHO_RULES["prefix"][prefix])
        if suffix:
            guess.append(MORPHO_RULES["suffix"][suffix])
        return " ".join(guess)
    return "❓"

def auto_add_to_lexicon(word, pos, gloss, lexicon_path="voynich_lexicon_expanded_quality.json"):
    with open(lexicon_path, "r", encoding="utf-8") as f:
        lexicon = json.load(f)
    if word not in lexicon:
        lexicon[word] = {"pos": pos, "meaning": gloss}
        with open(lexicon_path, "w", encoding="utf-8") as f:
            json.dump(lexicon, f, indent=2, ensure_ascii=False)
        return True
    return False

def explain_morphology(word):
    parts = {}
    for p, meaning in MORPHO_RULES["prefix"].items():
        if word.startswith(p):
            parts["prefix"] = (p, meaning)
    for s, meaning in MORPHO_RULES["suffix"].items():
        if word.endswith(s):
            parts["suffix"] = (s, meaning)
    return parts
