from itertools import *
def all_variants(text):
    for a in range(0,len(text)):
        g=text[a]
        yield g
    for b in range(0, len(text)-1):
        c = text[b]+text[b+1]
        yield c
    d = text
    yield d
    
a = all_variants('abc')
for i in a:
    print(i)