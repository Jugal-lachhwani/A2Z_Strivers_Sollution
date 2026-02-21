s = "LVIII"

def roman_to_int(s):
    d = {"I":1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    i = 0
    
    while i < len(s)-1:
        
        if d[s[i+1]] <= d[s[i]]:
            num += d[s[i]]
            if i+1 == len(s)-1:
                num += d[s[i+1]]
            
        else:
            num += (d[s[i+1]] - d[s[i]])
            i += 1
        i += 1
    
    return num

print(roman_to_int(s))
