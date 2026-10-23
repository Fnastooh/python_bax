num = [5,24,9,6,7,15,11,8,13]

n = len(num)

for i in range(n-1):
    for j in range(n-i-1):
        if num[j] > num[j+1]:
          #  num[j], num[j+1] = num[j+1], num[j]
            temp = num[j]
            num[j] = num[j+1]
            num[j+1] = temp


print(num)

#finish