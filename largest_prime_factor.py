def primeFactor(number):
    largest_pf = 0          
    lowest_pef = 2                     # start from the lowest even prime factor we know
    sqroot = number ** 0.5        # this would be used to stop the loop since it would be redundant to keep going past the squareroot( this is because it reduces on the right side (b) as the left increases (a))
    while lowest_pef <= sqroot:
        if number % lowest_pef == 0: 
            number = number / lowest_pef
            if largest_pf < lowest_pef:
                largest_pf = lowest_pef
                print(largest_pf)
        else:
            lowest_pef += 1    # increase the divisor when it can't divide without a remainder
    return largest_pf


print(primeFactor(600851475143))
print(600851475143 ** 0.5)
