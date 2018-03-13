def drawgrid(x):
    a = 4 * '- ' + '+ ' #horizontal edge of one cell
    b = 4 * '  ' + '| ' #inner part of one cell
    
    aa = '+ ' + x*a + '\n' #horizontal edge of whole grid
    bb = '| ' + x*b + '\n' #inner part of whole grid
    
    row = 4*bb + aa #one row of cells
        
    print aa + x*row #print the whole grid
    
drawgrid(4)
