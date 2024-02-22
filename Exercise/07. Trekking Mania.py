groups = int(input())

musala = int()
monblanc = int()
kalimandjaro = int()
k2 = int()
everest = int()

for i in range(0, groups):
    size_of_group = int(input())

    if size_of_group <= 5:
        musala += size_of_group
    elif size_of_group <= 12:
        monblanc += size_of_group
    elif size_of_group <= 25:
        kalimandjaro += size_of_group
    elif size_of_group <= 40:
        k2 += size_of_group
    else:
        everest += size_of_group

total_participants = musala + monblanc + kalimandjaro + k2 + everest

print(f'{(musala / total_participants) * 100:.2f}%')
print(f'{(monblanc / total_participants) * 100:.2f}%')
print(f'{(kalimandjaro / total_participants) * 100:.2f}%')
print(f'{(k2 / total_participants) * 100:.2f}%')
print(f'{(everest / total_participants) * 100:.2f}%')
