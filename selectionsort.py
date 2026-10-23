numbers = [ 4,7,3,7,2,7,4,3, 12 ,45,32,5,7,9,3,2,55,88,53,8,95,3,51,3,5,64]

n = len(numbers)


for i in range(n-1):
    min = numbers[i]
    MinIndex = i
    for j in range(i+1, n):
        if numbers[j] < min:
            min = numbers[j]
            MinIndex = j
    if MinIndex != -1:
        temp = numbers[i]
        numbers[i] = numbers[MinIndex]
        numbers[MinIndex] = temp

print(numbers)