def primeSum(n):
    initial = [True] * (n+1)
    initial[0] = initial[1] = False

    p = 2

    while p*p <= n:
        if initial[p]:
            for i in range(p*p, n+1, p):
                initial[i] = False
        p+=1

    return sum(i for i in range(len(initial)) if initial[i])
 

print(primeSum(2000000))