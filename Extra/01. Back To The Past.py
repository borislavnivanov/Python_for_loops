inheritance = float(input())
final_year = int(input())

spent_money = float()
age = 18

for i in range(1800, final_year + 1):
    if i % 2 == 0:
        spent_money += 12000
    else:
        spent_money += 12000 + (age * 50)

    age += 1

if spent_money <= inheritance:
    print(f'Yes! He will live a carefree life and will have {inheritance - spent_money:.2f} dollars left.')
else:
    print(f'He will need {abs(inheritance - spent_money):.2f} dollars to survive.')
