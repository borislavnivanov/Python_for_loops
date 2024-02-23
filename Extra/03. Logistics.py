cargoes = int(input())

microbus = 0
truck = 0
train = 0

for i in range(0, cargoes):
    tons = int(input())
    if tons <= 3:
        microbus += tons
    elif tons <= 11:
        truck += tons
    else:
        train += tons

total_tons = microbus + truck + train

average_price = (microbus * 200.00 + truck * 175 + train * 120) / total_tons

print(f'{average_price:.2f}')
print(f'{(microbus / total_tons) * 100:.2f}%')
print(f'{(truck / total_tons) * 100:.2f}%')
print(f'{(train / total_tons) * 100:.2f}%')
