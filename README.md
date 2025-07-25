# Voynich Translator Toolkit

> AI-assisted grammar-based decoding framework for the Voynich Manuscript  
> Developed by **Dong-Yeon Kang** | Digital Hollywood University

---

## 🌐 Overview

The Voynich Manuscript has resisted decipherment for over a century.  
This project introduces a **rule-based translation system** that approaches the manuscript as a **structured language** with consistent internal grammar, rather than a cipher.

The translator integrates:
- EVA (European Voynich Alphabet) token analysis
- Morphological grammar rules (prefix, root, suffix)
- Semantic ontology for meaning inference
- Bidirectional translation (Voynich ↔ English)
- Reproducible test sets with scoring metrics

---

## 📁 Project Structure

| File/Folder             | Description |
|-------------------------|-------------|
| `run_examples.py`       | Demo script: forward & reverse translation |
| `translate.py`          | EVA → English decoder |
| `reverse.py`            | English → EVA reverse translator |
| `sentence_parser.py`    | Morphological parser |
| `semantic_score.py`     | Scoring system for translation quality |
| `voynich_lexicon_expanded.json` | Main vocabulary (POS + glosses) |
| `morphology_rules.json` | Suffix/prefix → semantic patterns |
| `ontology.json`         | Conceptual mapping (e.g., sky, life, water) |

---

## 🧪 Example Usage

```bash
python run_examples.py
