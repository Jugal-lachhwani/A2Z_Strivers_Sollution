s = "tttrree"

def sort_by_freq(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
        
    return sorted(d, key=lambda x: d[x], reverse=True)

print(sort_by_freq(s))
