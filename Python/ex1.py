print "Hello World!"
print
print "This is Joe's world."
#print 'This is Joe's world.'
print
print "Did you say 'Joe'?"
print 'I said "Joe".'
print #This is a comment...
print "25 + 30 / 6 =", 25+30/6
print "25 * 3 % 4 =", 25*3%4

print #Modulo has higher precedence!

print "75 % 4 =", 75%4
print "75 / 4 =", 75/4
print 75/4, "* 4 =", 75/4*4

print #Division and multiplication have equal precedence.

print "15 / (4 * 4) =", 15/(4*4)
print "16 / (4 * 4) =", 16/(4*4)
print
print "Floating point: ", 15.0/(4*4)
print
print "2 + 2 = 5 ?", "Yes!" if 2+2==5 else "No!"
print "This statement is", 2+2==5, "!"

print #Doesn't work: 2+2==5 ? "Yes!" : "No!"
#http://en.wikipedia.org/wiki/Ternary_operation

print "It is", 4==5, "\b!"
print "Es ist", 4==5, "\b\bch!"
print
#print "Division by zero: ", 1/0
