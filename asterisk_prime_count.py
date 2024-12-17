import math

def isPrime(n):

    for i in range(3, int(math.sqrt(n)), 2): # stopping at the sqrt to reduce unnecessary runs
        if n % i == 0:
            return False
        
    return True

def primeCount(index):
    number = 3 #skipping 2 since it's the only even prime number
    count = 1
    while True:
        if isPrime(number):
            count +=1
            if count == index:
                return number
        
        number+=2 #only checking for odd numbers


print(primeCount(10001))