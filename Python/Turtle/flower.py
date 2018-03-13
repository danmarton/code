from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.005

def drawarc(t,r,a):
    for i in range(a):
        fd(t,2*r*math.pi/360)
        lt(t,1)

def drawpetal(t,r,a):
    drawarc(t,r,a)
    lt(t,180-a)
    drawarc(t,r,a)

def drawflower(t,l,n):
    rad = 2*math.pi/n
    r = l/(2*math.sin(rad/2))
    
    for i in range(n):
        drawpetal(t,r,360/n)
        lt(t,180)
    pu(t)
    fd(t,l)
    pd(t)
    lt(t)
    drawarc(t,l,360)
    
def drawflower2(t,l,n):
    n=n/2
    t.delay=0.001
    rad = 2*math.pi/n
    r = l/(2*math.sin(rad/2))
    
    for i in range(2*n):
        drawpetal(t,r,360/n)
        lt(t,180-360/(2*n))
    pu(t)
    fd(t,l)
    pd(t)
    lt(t)
    drawarc(t,l,360)

drawflower2(bob,150,8)

wait_for_user()
