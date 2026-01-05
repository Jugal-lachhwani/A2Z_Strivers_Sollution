"""Merge Sort Algorithm

Problem Statement: Given an array of size n, sort the array using Merge Sort

"""


def merge(l,r):
    i,j,m,n,c = 0,0,len(l),len(r),[]

    while i+j < m+n:
        if i == m:
            c.append(r[j])
            j += 1
        elif j == m:
            c.append(l[i])
            i+=1
        elif l[i] > r[j]:
            c.append(r[j])
            j+=1
        else:
            c.append(l[i])
            i+=1
    return c

arr = [4,1,7,9,3,5,6,2,1]
def mergesort(arr):
    if len(arr) < 2:
        return arr
    left = mergesort(arr[0:len(arr)//2])
    right = mergesort(arr[len(arr)//2:len(arr)])  
    return merge(left,right)

mergesort(arr)