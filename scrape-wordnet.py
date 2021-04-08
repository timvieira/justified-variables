from nltk.corpus import wordnet as wn
from collections import defaultdict


def meronyms():
    for x in wn.all_synsets():
        if not x.part_meronyms(): continue

        # what are all the different (meronyms) parts that x is made of?
        lengths = defaultdict(lambda: defaultdict(list))

        #parts = x.substance_meronyms()
        parts = x.part_meronyms()
        for y in parts:
            # if there is already a synonym
            for yy in y.lemma_names():
                lengths[len(yy)][y].append(yy)

        if any(len(z) > 1 for z in lengths.values()):
            print()
            print(f'> {x} has {len(parts)} parts.')
            for n in lengths:
                if len(lengths[n]) > 1:
                    yyy = []
                    for y in lengths[n]:
                        yyy.append('/'.join(yy for yy in lengths[n][y]))

                    print(f'{n}: {", ".join(yyy)}')

#meronyms()


def hypernyms():
    V = set()

    for X in wn.all_synsets():
        for Y in X.hypernyms():

            for x in X.lemma_names():
                for y in Y.lemma_names():

                    if len(x) == len(y):
                        V.add(tuple(sorted([x, y])))

    for x, y in sorted(V, key=lambda z: (len(z[0]), z)):
        print(x, y)

    print()
    print(f'found {len(V)} pairs')



def antonyms():
    V = set()

    for syn in wn.all_synsets():
        for l in syn.lemmas():
            x = l.name()
            for Y in l.antonyms():
                y = Y.name()
                if len(x) == len(y):
                    V.add(tuple(sorted([x, y])))

    for x, y in sorted(V, key=lambda z: (len(z[0]), z)):
        print(x, y)

    print()
    print(f'found {len(V)} pairs')


#hypernyms()
#antonyms()


def syns(x):
    for sense in wn.synsets(x):
        for lemma in sense.lemmas():
            x = lemma.name()
            yield x


def suggest(x, y):
    for xx in sorted(set(syns(x)), key=lambda xx: (len(xx), x)):
        for yy in sorted(set(syns(y))):
            if len(xx) == len(yy):
                print(xx, yy)

#suggest('vertices', 'edges')
#suggest('start', 'stop')
suggest('grow', 'shrink')
