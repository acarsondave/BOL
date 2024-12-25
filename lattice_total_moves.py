def factorial(n):
    for i in range(1, n):
        n*=i
    return n


def totalMoves(n):
    
    upper = factorial(n*2)
    lower = factorial(n) * factorial(n)
    
    return upper//lower
    
    
print(totalMoves(20))