
from lexicon_helper import suggest_gloss, explain_morphology

def rank_gloss_candidates(word):
    explanation = explain_morphology(word)
    gloss = suggest_gloss(word)
    return {
        "word": word,
        "explanation": explanation,
        "suggested_gloss": gloss
    }

if __name__ == "__main__":
    word = input("Enter EVA word: ")
    result = rank_gloss_candidates(word)
    for k, v in result.items():
        print(f"{k}: {v}")
