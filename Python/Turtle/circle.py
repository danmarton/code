from swampy.TurtleWorld import *
import math

def drawcircle(t, r):
    pu(t)
    fd(t,r)
    lt(t)
    pd(t)
    for i in range(36):
        fd(t,2*r*math.pi/36) #forward
        lt(t,10) #left turn

world = TurtleWorld()
bob = Turtle()

bob.delay = 0.01
drawcircle(bob,160)

wait_for_user()
