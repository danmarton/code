cylinder :: Float -> Float -> Float
cylinder r h = let
    side = 2*r*pi * h
    top = r^2*pi  
    in side + 2 * top
