bodymass :: Float -> Float -> String
bodymass :: Float -> Float -> String
bodymass weight_kg height_m
    | bmi < s = show bmi ++ " emo"
    | bmi < m = show bmi ++ " normal"
    | bmi < l = show bmi ++ " fat"
    | otherwise  = show bmi ++ " lard-ass"
    where height = if height_m>100 then height_m/100 else height_m
          bmi = weight_kg / height^2
          (s,m,l) = (18.5,25.0,30.0) -- Pattern matching!
