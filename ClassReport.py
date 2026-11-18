marks = [18, 12, 9, 20, 15, 7, 16, 11, 19, 13, 14, 8, 17, 10, 6, 19, 15, 12, 20, 9]

n = len(marks)

Averageog = 0
passed = 0
failed = 0

for i in marks:
    Averageog += i

Average = Averageog / n

max_num = marks[0]

for i in marks:
    if i > max_num:
        max_num = i

min_num = marks[0]

for i in marks:
    if i < min_num:
        min_num = i

for i in range(n):
    if marks[i] >= 10:
        passed += 1
    else:
        failed += 1

print(f"""
---Report---
Average: {Average}
Highest Mark: {max_num}
Lowest Mark: {min_num}
Passed Students: {passed}
Failed Students: {failed}
""")