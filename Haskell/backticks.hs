-- Infix notation can be used in definitions as well!

myCompare :: (Ord a) => a -> a -> Ordering  

a `myCompare` b
    | a > b     = GT  
    | a == b    = EQ  
    | otherwise = LT
