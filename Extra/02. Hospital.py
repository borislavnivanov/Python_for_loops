period = int(input())

practitioners = 7
serviced = 0
sent_out = 0

for i in range(1, period + 1):
    patients_arrived = int(input())
    if i % 3 == 0:
        if sent_out > serviced:
            practitioners += 1

    if patients_arrived >= practitioners:
        serviced += practitioners
        sent_out += patients_arrived - practitioners
    else:
        serviced += patients_arrived

print(f'Treated patients: {serviced}.')
print(f'Untreated patients: {sent_out}.')
