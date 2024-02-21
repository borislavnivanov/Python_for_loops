count = int(input())

left_side = 0
right_side = 0

for i in range(0, count):
    left_side += int(input())

for i in range(0, count):
    right_side += int(input())

if left_side == right_side:
    print(f'Yes, sum = {left_side}')
else:
    print(f'No, diff = {abs(left_side - right_side)}')
