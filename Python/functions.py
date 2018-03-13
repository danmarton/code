from string import join

def printargs(*args):
	for x in args: print x,
	print

def giveargs(*args):
	return join(args)

printargs("dani","jo","fej")

print giveargs("dani","jo","fej")

def prr(a): print a
def prr(a,b): print a,b

prr(1)
prr(1,2)
