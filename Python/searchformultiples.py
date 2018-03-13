result = [1,2,3,1,4,2,5,6,4,7,8]

for x in result:
    ssum = 0
    for y in result:
        if x==y: ssum+=1
    if ssum>1: print x
