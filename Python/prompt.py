from sys import argv

script, user_name = argv
prompt = 'Prompt: '

print "Hi %s, I'm %s!" % (user_name, script)

print "What do you want to say?"
likes = raw_input(prompt)

print "Where do yo live?"
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
You said %r.
You live in %r.
You have a %r computer.
""" % (likes, lives, computer)
