import sys

count = int(input())
min_number = sys.maxsize
max_number = -sys.maxsize

for i in range(0, count):
    number = int(input())

    if number < min_number:
        min_number = number

    if number > max_number:
        max_number = number

print('Max number: ' + str(max_number))
print('Min number: ' + str(min_number))
