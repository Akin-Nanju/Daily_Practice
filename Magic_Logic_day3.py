def magic_square(grid):
    sumC = 0
    n = len(grid)
    print(n)
    diagnal = []
    for row in grid:
        sumC += row[0]  
    print("Sum of first column:", sumC)
    sumC1 = 0
    for col in grid:
        sumC1 += col[1]
    print("Sum of second column:",sumC1)
    sumC2 = 0
    for col in grid:
        sumC2 += col[2]
    print("Sum of third column:",sumC2)
    for i in range(n):
        diagnal.append(grid[i][i])
    print("Sum of diagnol is:",sum(diagnal))
    if sumC == sumC1 == sumC2 == sum(diagnal):
        return "MAGIC NUMBER"
    else:
        return "NOT MAGIC NUMBER"
    
    
    
a = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]
print(magic_square(a))