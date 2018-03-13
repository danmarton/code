text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

result = ""

for x in text:
    if ord(x) >= ord('a') and ord(x) <= ord('z'):
        result += chr( (ord(x)-ord('a')+2) % 26 + ord('a') )

#1. Place of letter in latin alphabet is ord(x)-ord(a)
#2. Add 2 to this value to shift the letter
#3. Adding 2 to Y or Z would make more than 26 -> modulo is used to subtract 26
#This places them to A and B respectively.
#3. Finally, add ord(a) back so that new place of letter becomes an ascii value

    else: result += x #Do not change non-letter characters.
    
print result
