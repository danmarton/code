import itertools, string

mess = open('/home/dan/Python/Challenge/mess2.txt').read()

result = list()
six = mess[:7]
    
for a in mess[7:]:
    if six[:3]==six[-1:-4:-1]: result.append(six)
    six = six[1:]
    six += a
    
for x in result: print x
