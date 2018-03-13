import string

table = string.maketrans("abcd","1234")

print string.translate("dani", table)

print "dani".translate(table)

dani = "dani"

print dani.translate(table)
