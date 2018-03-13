from swampy.TurtleWorld import *

def drawpolygon(t, l, s):
    for i in range(s):
        fd(t,l)
        lt(t,360/s)

world = TurtleWorld()
bob = Turtle()

drawpolygon(bob,50,9)

wait_for_user()
