import itertools, string

mess = open('/home/dan/Python/Challenge/mess2.txt').read()
mess.replace("\n","")

result = list()
six = mess[:9]
small = string.ascii_lowercase
big = string.ascii_uppercase
    
for a in mess[9:]:
    if small.count(six[4])>0:
        there = True
        for c in six[1:4]+six[5:8]: 
            if big.count(c) == 0: there = False
        if big.count(six[0]) != 0 or big.count(six[8]) != 0: there = False
        if there: result.append(six)
    six = six[1:]
    six += a

for x in result: print x
