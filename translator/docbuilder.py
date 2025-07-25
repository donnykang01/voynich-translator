
import json

def build_readme():
    with open("voynich_lexicon_expanded_quality.json", "r", encoding="utf-8") as f:
        lexicon = json.load(f)
    total_words = len(lexicon)
    example_words = list(lexicon.items())[:5]

    lines = [
        "# Voynich Translator Toolkit",
        "",
        "## Summary",
        f"- Total words in lexicon: {total_words}",
        f"- Example entries:",
    ]
    for word, entry in example_words:
        lines.append(f"  - {word}: ({entry['pos']}) {entry['meaning']}")

    lines.append("")
    lines.append("## Modules Included")
    lines.append("- `translate.py` - Translate EVA to English")
    lines.append("- `reverse.py` - Reverse English to EVA")
    lines.append("- `lexicon_helper.py` - Suggest or insert unknown glosses")
    lines.append("- `sentence_parser.py` - Parse sentence into structure")
    lines.append("- `semantic_score.py` - Evaluate sentence quality")
    lines.append("- `auto_gloss_ranker.py` - Gloss suggestion and ranking")
    lines.append("- `docbuilder.py` - Auto-document generator")
    lines.append("")
    lines.append("## License")
    lines.append("Released under CC BY 4.0 – Dong-Yeon Kang (Digital Hollywood University)")

    with open("README_autobuilt.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
