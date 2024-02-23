moves = int(input())

result = 0
numbers_9 = 0
numbers_19 = 0
numbers_29 = 0
numbers_39 = 0
numbers_50 = 0
numbers_inv = 0

for i in range(0, moves):
    move = int(input())

    if move < 0 or move > 50:
        result /= 2
        numbers_inv += 1
    elif move <= 9:
        result += move * 0.20
        numbers_9 += 1
    elif move <= 19:
        result += move * 0.30
        numbers_19 += 1
    elif move <= 29:
        result += move * 0.40
        numbers_29 += 1
    elif move <= 39:
        result += 50
        numbers_39 += 1
    elif move <= 50:
        result += 100
        numbers_50 += 1

total_moves = numbers_9 + numbers_19 + numbers_29 + numbers_39 + numbers_50 + numbers_inv

print(f'{result:.2f}')
print(f'From 0 to 9: {(numbers_9 / total_moves) * 100:.2f}%')
print(f'From 10 to 19: {(numbers_19 / total_moves) * 100:.2f}%')
print(f'From 20 to 29: {(numbers_29 / total_moves) * 100:.2f}%')
print(f'From 30 to 39: {(numbers_39 / total_moves) * 100:.2f}%')
print(f'From 40 to 50: {(numbers_50 / total_moves) * 100:.2f}%')
print(f'Invalid numbers: {(numbers_inv / total_moves) * 100:.2f}%')
