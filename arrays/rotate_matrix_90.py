"""
Rotate Image by 90 degree

Problem Statement: Given an N * N 2D integer matrix, rotate the matrix by 90 
degrees clockwise. The rotation must be done in place, meaning the input 2D 
matrix must be modified directly.

Approach: This solution creates a new matrix. 
For in-place: 1) Transpose the matrix, 2) Reverse each row.
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def matrix_rotate(matrix):
    r = len(matrix)
    c = len(matrix[0])
    new_mat = [[0]*c for _ in range(r)]
    nm = -1
    for j in range(c):
        nm = 0
        for i in range(r-1,-1,-1):
            print(j,nm,matrix[i][j])
            new_mat[j][nm] = matrix[i][j]
            nm+=1
            
    return new_mat

print(matrix_rotate(matrix))
