def getPrimelist(n):
    initial = [True] * (n + 1)
    initial[0] = initial[1] = False
    p = 2
    while p * p <= 20:
        if initial[p]:
            for i in range(p*p, n+1, p):
                initial[i] = False
        p+=1
    return [i for i in range(len(initial)) if initial[i]]


def smallestMultiple(highest): 
    prime_f = getPrimelist(highest)
    result = 1
    for k in prime_f:
        current = k
        for i in range(1, highest+1):
            if k**i <= highest:
                current = k ** i
            else:
                break
        result*=current
    return result

print(smallestMultiple(20))