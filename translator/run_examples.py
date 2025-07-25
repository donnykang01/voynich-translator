
from translate import load_lexicon, process_line
from reverse import reverse_lookup

lexicon = load_lexicon()

print("=== Forward Translation ===")
sample = "qokedy okaiin dytorar"
result = process_line(sample, lexicon)
for token, pos, meaning in result:
    print(f"{token:<10} | {pos:<10} | {meaning}")

print("\n=== Reverse Translation ===")
english = "simulated meaning for okaiin"
voynich = reverse_lookup(english, lexicon)
print(f"{english} => {voynich}")
