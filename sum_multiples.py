def multiples(n, m):
    results = 0
    for i in range(1, 1001):
        if i % n == 0 or i % m == 0:
          results += i
    return results


print(multiples(3, 5))

