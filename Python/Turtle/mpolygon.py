from swampy.TurtleWorld import *
import math

def mpolygon(t, l, s):
    deg = 360/s
    rad = 2*math.pi/s
    r = l/2/math.sin(rad/2)
    beta = 90-deg/2
    
    rt(t,90+deg/2)
    
    for i in range(s):
        fd(t,r)
        lt(t,90+deg/2)
        fd(t,l)
        lt(t,deg+beta)
        fd(t,r)
        rt(t,180)
        
world = TurtleWorld()
bob = Turtle()
bob.delay=0.1

mpolygon(bob,100,12)

wait_for_user()
