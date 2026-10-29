numbers = [10, 2, 12, 8, 3, 15, 3, 5, 64]

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
