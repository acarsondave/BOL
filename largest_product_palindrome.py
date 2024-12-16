def findProductPalindrome(num1, num2):
    largest = 0
    while True:
        
        if num1 > 999:
            return largest

        if num2 > 999:
            num2-=900
            num1+=1
        
        check = num1 * num2
    
        if str(check) == str(check)[::-1]:
            if check > largest:
                largest = check
        
        num2+=1

print(findProductPalindrome(100, 100))