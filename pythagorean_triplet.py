def findTriplet(n):
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if a+b+c == n:
                    if (a ** 2) + (b ** 2) == (c ** 2):
                        print(f"Found Triplet: {a}, {b}, {c}")
                        return a*b*c

       



print(findTriplet(1000))