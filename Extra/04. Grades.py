students = int(input())

count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0

average_sum = 0

for i in range(0, students):
    score = float(input())
    average_sum += score
    if score < 3.00:
        count_2 += 1
    elif score < 4.00:
        count_3 += 1
    elif score < 5.00:
        count_4 += 1
    else:
        count_5 += 1

total_scores = count_2 + count_3 + count_4 + count_5
average_sum = average_sum / total_scores

print(f'Top students: {(count_5 / total_scores) * 100:.2f}%')
print(f'Between 4.00 and 4.99: {(count_4 / total_scores) * 100:.2f}%')
print(f'Between 3.00 and 3.99: {(count_3 / total_scores) * 100:.2f}%')
print(f'Fail: {(count_2 / total_scores) * 100:.2f}%')
print(f'Average: {average_sum:.2f}')
