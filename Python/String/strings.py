x = "There are %d types of people." % (10 + 5)
binary = "binary"
dont = "don't"
y = "Those who know %s and those who %s." % (binary, dont)

print x
print y

print "I said: %r" % x
print "I also said: '%s'" %y

hilarious = False
evaluation = "Isn't that joke so funny?! %r"

print evaluation % hilarious

w = "This is the left side of "
e = "a string with a right side."

print w + e
