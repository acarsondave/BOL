# def evenFibonacciRecursion(limit, even):  # This method did not work because of the recursion depth error, could not reach the 4 million required.
#     if limit > 990:
#          return even
    
#     if limit % 2 == 0:
#          print(limit)
#          even += limit

#     return evenFibonacciRecursion(limit+1, even)

def evenFibonacci(fibonacci_seq):
    count = 0
    while fibonacci_seq[-1] < 4000000:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[count])
        count += 1
    return sum(i for i in fibonacci_seq if i % 2 == 0)

print(evenFibonacci([1,2]))