str = open('/home/dan/Python/Challenge/mess.txt').read()

lst = list()

for i in range(256): lst.append(0)

for c in str: lst[ord(c)]+=1

ls2 = list()

for i in range(256): 
    if lst[i]==1: ls2.append(chr(i))

st2=""

for c in str:
    boo=False
    for j in ls2:
        if c==j: boo=True
    if boo: st2+=c
    
print st2
