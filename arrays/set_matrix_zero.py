"""
Set Matrix Zero

Problem Statement: Given a matrix if an element in the matrix is 0 then you 
will have to set its entire column and row to 0 and then return the matrix.

Approach: First pass - identify all rows and columns containing zeros using sets.
Second pass - set elements to 0 if their row or column was marked.
"""

matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

def set_zero(matrix):
    r = len(matrix)
    c = len(matrix[0])
    
    row = set()
    col = set()
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
                
    for i in range(r):
        for j in range(c):
            if i in row or j in col:
                matrix[i][j] = 0
    return matrix

print(set_zero(matrix))
