stadium_capacity = int(input())
amount_fans = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for i in range (amount_fans):
    sector = input()

    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1

total_fans = sector_a + sector_b + sector_v + sector_g

print(f'{sector_a / amount_fans * 100:.2f}%')
print(f'{sector_b / amount_fans * 100:.2f}%')
print(f'{sector_v / amount_fans * 100:.2f}%')
print(f'{sector_g / amount_fans * 100:.2f}%')
print(f'{total_fans / stadium_capacity * 100:.2f}%')
