def minor_diagonal_sum(matrix):
    n=len(matrix)
    diagonal_sum=0
    for i in range(n):
            diagonal_sum+=matrix[i][n-i-1]
    return diagonal_sum
rows,columns=map(int,input().split())
matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
diagonal_sum = minor_diagonal_sum(matrix)
print(diagonal_sum)



