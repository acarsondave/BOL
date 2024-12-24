def sequence(length):
    pos = length
    largest = 0
    number = 0
    for _ in range(1, length+1):
        count = 1
        start = pos
        while start > 1:
            if start % 2 == 0:
                start = start//2
                count+=1
            else:
                start = (start * 3) + 1
                count+=1
        if count > largest:
            largest = count
            number = pos
        pos-=1
    return number, largest

print(sequence(999999))