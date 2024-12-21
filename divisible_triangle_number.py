def divisibleTriangle(divisors):
    n = 1
    while True:
        x = (n * (n+1)) // 2
        divnum = []
        count = 0
        
        for k in range(1, int((x**0.5) + 1)):
            if x % k == 0:
                if k != x//k:
                    divnum.append(k)
                    divnum.append(x//k)
                    count+=2
                else:   
                    divnum.append(k)             
                    count+=1
                
        if count >= divisors:
            return f"TriangleNumber: {x}\nDivisors: {sorted(divnum)}\nLength: {len(divnum)}\n==================================================="
        
        n+=1
            
print(divisibleTriangle(500))