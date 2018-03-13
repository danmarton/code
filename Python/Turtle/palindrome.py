def palin(word):
    if len(word)<=2: 
        return word[0] == word[-1]
    else: 
        return palin(word[1:-1])
        
palin("indulagorogaludni")
