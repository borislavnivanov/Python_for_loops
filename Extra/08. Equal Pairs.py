from sys import maxsize

min_sum = maxsize
max_sum = -maxsize

number_pairs = int(input())

for i in range(0, number_pairs):
    value_1 = int(input())
    value_2 = int(input())

    pair_sum = value_1 + value_2

    if pair_sum > max_sum:
        max_sum = pair_sum
        if min_sum == maxsize:
            min_sum = pair_sum

    else:
        min_sum = pair_sum



if max_sum == min_sum:
    print(f'Yes, value={max_sum}')
else:
    print(f'No, maxdiff={abs(max_sum - min_sum)}')
