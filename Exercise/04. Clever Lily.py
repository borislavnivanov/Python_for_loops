age = int(input())
price_washer = float(input())
price_toy = float(input())

gifted_money = float()
toys_pc = int()
toys_money = float()
multiplier = int()

for i in range(1, age + 1):

    if i % 2 == 0:
        multiplier += 1
        gifted_money += 10 * multiplier
        gifted_money -= 1
    else:
        toys_pc += 1

toys_money = toys_pc * price_toy

total = gifted_money + toys_money

if total >= price_washer:
    print(f'Yes! {total - price_washer:.2f}')
else:
    print(f'No! {abs(total - price_washer):.2f}')
