count = int(input())

counter_200 = 0
counter_399 = 0
counter_599 = 0
counter_799 = 0
counter_1000 = 0

for i in range(0, count):
    number = int(input())
    if number < 200:
        counter_200 += 1
    elif number <= 399:
        counter_399 += 1
    elif number <= 599:
        counter_599 += 1
    elif number <= 799:
        counter_799 += 1
    else:
        counter_1000 += 1

print(f'{(counter_200 / count) * 100:.2f}%')
print(f'{(counter_399 / count) * 100:.2f}%')
print(f'{(counter_599 / count) * 100:.2f}%')
print(f'{(counter_799 / count) * 100:.2f}%')
print(f'{(counter_1000 / count) * 100:.2f}%')
