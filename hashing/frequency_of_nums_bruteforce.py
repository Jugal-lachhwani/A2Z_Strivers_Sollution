"""Brute Force"""

cnt_l = []
for num in q:
    cnt = 0
    for i in l:
        if i == num:
            cnt += 1
    cnt_l.append(cnt)
    
print(cnt_l)