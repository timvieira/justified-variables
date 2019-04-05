from nltk.corpus import wordnet as wn

V = set()

for syn in wn.all_synsets():
    for l in syn.lemmas():
        x = l.name()
        if l.antonyms():
            y = l.antonyms()[0].name()
            if len(x) == len(y):
                V.add(tuple(sorted([x, y])))

for x, y in sorted(V, key=lambda z: (len(z[0]), z)):
    print(x, y)

print()
print(f'found {len(V)} pairs')
