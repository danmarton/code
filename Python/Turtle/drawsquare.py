from swampy.TurtleWorld import *

def drawsquare(t, l):
    for i in range(4):
        fd(t,l) #forward
        lt(t) #left turn

world = TurtleWorld()
bob = Turtle()

drawsquare(bob, 100)

wait_for_user()
