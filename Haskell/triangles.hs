triangles = [(a,b,c) | c<-[1..],b<-[1..c],a<-[1..b], a^2+b^2==c^2]
-- C has to be in scope before B can be defined as [1..c]
-- This is more efficient than each being [1..]
-- And it also avoids the repetition of identical triangles

triang12 = [(a,b,c) | (a,b,c)<-triangles, mod (a+b+c) 12 = 0]
