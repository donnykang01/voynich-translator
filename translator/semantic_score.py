
def score_parsed_sentence(parsed, meaning_to_category):
    score = 0
    details = []
    for i, word in enumerate(parsed):
        if word["pos"] == "Unknown" or word["meaning"] == "❓":
            score -= 2
            details.append(f"- [{word['eva']}] unknown meaning or POS")
        if i > 0:
            prev_pos = parsed[i - 1]["pos"]
            curr_pos = word["pos"]
            if prev_pos == "Noun" and curr_pos == "Noun":
                score -= 1
                details.append(f"- [{parsed[i-1]['eva']}, {word['eva']}] noun-noun adjacency")
            if prev_pos == "Prep" and curr_pos != "Noun":
                score -= 1
                details.append(f"- [{parsed[i-1]['eva']}, {word['eva']}] prep not followed by noun")
        if i > 0:
            prev_cat = meaning_to_category.get(parsed[i - 1]["meaning"])
            curr_cat = meaning_to_category.get(word["meaning"])
            if prev_cat and curr_cat and prev_cat == curr_cat:
                score += 1
                details.append(f"+ [{parsed[i-1]['eva']}, {word['eva']}] same semantic group")
    return score, details
