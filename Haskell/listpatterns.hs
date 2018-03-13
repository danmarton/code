head' :: [a] -> a
head' [] = error "I got nothin'!"
head' (x:_) = x

firsttwo :: [a] -> (a,a)
firsttwo [] = error "I got nothin'!"
firsttwo (x:[]) = (x,x)
firsttwo (x:y:_) = (x,y)

length' :: Num b => [a] -> b  
length' [] = 0  
length' (_:xs) = 1 + length' xs  

tell :: (Show a) => [a] -> String  
tell [] = "The list is empty"  
tell (x:[]) = "The list has one element: " ++ show x  
tell (x:y:[]) = 
    "The list has two elements: " 
    ++ show x ++ " and " ++ show y  
tell (x:y:_) = 
    "This list is long. The first two elements are: " 
    ++ show x ++ " and " ++ show y
