def sumofSquares(n):
    return (sum([i for i in range(1, n+1)]) ** 2) - sum([i ** 2 for i in range(1,n+1)])

print(sumofSquares(100))
