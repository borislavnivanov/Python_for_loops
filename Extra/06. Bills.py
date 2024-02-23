months = int(input())

electricity = 0.00
water = 20 * months
internet = 15 * months
other = 0.00

for i in range(months):
    current_el = float(input())
    electricity += current_el
    other += (current_el + 20 + 15) * 1.20

average_total = (electricity + water + internet + other) / months

print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average_total:.2f} lv')
