import itertools

asd = itertools.permutations('aeilqtuy')
    
for i in range(256):
    lst = asd.next()
    str=""
    for c in lst: str+=c
    print str
