power = int(input())

for i in range(0, power + 1):
    value = 2 ** i
    if i % 2 == 0:
        print(value)
