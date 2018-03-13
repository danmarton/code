s = "abcdabc"

print s.count("abc"), # looks for 'abc' in s
print s.count("abc",0,3), # looks for 'abc' in s[0:3]
print s.count("abc",4)>0 # Is 'abc' there in s[4:] ?
