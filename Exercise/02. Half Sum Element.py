import sys

count = int(input())

biggest_number = -sys.maxsize
sum = 0

for i in range(0, count):
    number = int(input())
    sum += number
    if number > biggest_number:
        biggest_number = number

if biggest_number == (sum - biggest_number):
    print(f'Yes\nSum = {biggest_number}')
else:
    print(f'No\nDiff = {abs(biggest_number - (sum - biggest_number))}')
