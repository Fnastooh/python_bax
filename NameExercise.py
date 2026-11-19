names = ["ali", "reza", "parsa", "amir", "mohammad", "hossein", "mehdi", "sina", "arman", "nima", "mahan", "kian", "arash", "soheil", "pouya", "sara", "nika", "zahra", "maryam", "ava", "yasmin", "mina", "negar", "sahar", "raha"]

names_two = []

names_one = []

user_output = []

x = input("Which name are you looking for?: ")

n = len(names)

for i in range(n):
    if 3 <= len(names[i]) <= 7:
        if i % 2 == 0:
            names_one.append(names[i])
        else:
            names_two.append(names[i])

for i in range(n):
    if x in names[i]:
        user_output.append(names[i])

print(names_one)
print(names_two)
print(f"Here is your names: {user_output}")
