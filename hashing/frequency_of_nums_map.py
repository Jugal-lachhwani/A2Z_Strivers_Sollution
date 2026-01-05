"""### How to hash large numbers like 10^9 or higher:
Until now, we have learned the method of number hashing but using this method we cannot hash large numbers like 109 or higher. We can solve this problem using the STL map and unordered_map in C++ or the HashMap in Java collection. Now, we are going to discuss these concepts in detail and most of the concepts are the same in map/unordered_map(in C++) and HashMap(in Java).

map and unordered_map in C++ / HashMap in Java:

Let’s understand the concepts considering the same example, we have used before, in the case of number hashing."""

d = {}

for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for num in q:
    if num in d:
        print(d[num])
    else:
        print(0)