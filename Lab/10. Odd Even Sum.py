count = int(input())

even = 0
odd = 0

for i in range(1, count + 1):
    if i % 2 == 0:
        even += int(input())
    else:
        odd += int(input())

if even == odd:
    print(f'Yes\nSum = {even}')
else:
    print(f'No\nDiff = {abs(even - odd)}')
