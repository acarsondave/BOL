def powerDigits(n, p):
    check = n**p
    add = sum([int(i) for i in str(check)])
    return add

print(powerDigits(2, 1000))
        