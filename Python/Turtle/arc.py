from swampy.TurtleWorld import *
import math

def drawarc(t, r, a):
    pu(t)
    fd(t,r)
    lt(t)
    pd(t)
    
    for i in range(a/10):
        fd(t,2*r*math.pi/36) #forward
        lt(t,10) #left turn
            
    remains = int(round((a/10.0-a/10)*2*r*math.pi/36))
    fd(t,remains)


world = TurtleWorld()
bob = Turtle()

bob.delay = 0.1
drawarc(bob,160,355)

wait_for_user()
