import sys, re

def CheckLine(s):
   
   if s[0] == '#' : return False
   
   if not re.match( "^\([^#(,)]+,[^#(,)]+\)$" , s ):
   
      raise SyntaxError(s.rstrip())
      
   return True
 
   
def ErrorString(message):
   
   return \
   """
   Bad syntax: %r

   Not allowed:
   - More than 2 parentheses
   - More than 1 comma
   - Comments not starting with '#' sign
   """ \
   % message


def GetEdges(f):
   
   return \
   [
      tuple( s.rstrip()[1:-1].split(',') )
      for s in f.readlines() 
      if CheckLine(s)
   ]
   

def GetVertices(edges):
   
   v = []
   
   for (a,b) in edges:
      if a not in v : v += [a]
      if b not in v : v += [b]
      
   return v
   
   
def Work(edg,ver,*workers):
   
   sched = {}
   work = [ g for g in ver if g not in [b for (a,b) in edg] ]
   left = ver
   nr = workers[0] if workers else len(edg)
   
   while left:      
      for (k,v) in zip(range(len(work)),work):
         if k%nr in sched: sched[k%nr] += v
         else: sched[k] = v
      
      nwork = [ g for g in ver if g in [b for (a,b) in edg if a in work] ]
      for w in work: left.remove(w)
      work = nwork
      
   return sched


def ShortestPath(sch): return max([len(b) for (a,b) in sch.items()])


#MAIN:

try:
   f = open( raw_input("File: ") )
   edges = GetEdges(f)
   n = int( raw_input("Number of workers: ") )
   
except IOError: 
   sys.exit("No such file can be read!")
except SyntaxError as e: 
   sys.exit(ErrorString(e.message))
except ValueError:
   print "No number given, assuming input to be null..."
   n = False
   
if n: schedule = Work(edges,GetVertices(edges),n)
else: schedule = Work(edges,GetVertices(edges))

print "Shortest path:", ShortestPath(schedule)
print "Number of workers:", len(schedule)

for (a,b) in schedule.items():
   print "Worker",a+1,":",b
