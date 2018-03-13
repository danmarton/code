#The colon indicates a range of indexes between the numbers standing left and right.
#list[x:y] -> list indexes starting with x, stopping at y.
#The index to the left is included but the index to the right is not!
#This is inspired by the for(int i=0; i<10; i++) in C-like languages.
#The iteration includes i=0, but not i=10

numbers = [0,1,2,3,4,5,6,7,8,9]
print
print numbers
print 
print numbers[2:] #lists from 3rd element until the very end.
print
print numbers[:2] #lists from the very start until the 3rd element.
print
print numbers[2:5] #lists from the 3rd, until the 6th.
print
print numbers[-1] #indexing from backwards, starting with -1.
print
print numbers[1:-2] #lists from 2nd until the 2nd last element.
print
print numbers[-3:] #lists the last 3 elements (that's why backward indexing starts with -1).
print
print numbers[-3:-1] #lists from 3d last until the last.
print
print numbers[2:9:2] #lists every second element from 3rd until 10th
                     #for(int i=0; i<9; i+=2)
print
print numbers[0::3] #lists every third element from the very start until the very end
print
print numbers[1::3] #every third, starting with the 2nd.
