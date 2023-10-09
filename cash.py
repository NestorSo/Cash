from cs50 import get_float

coins = 0
while True:
    Value = get_float("Ingrese el cambio ")
    if Value > 0:
        break
cents = round(Value * 100)

for i in [25, 10, 5, 1]:
    coins += cents // i
    cents = cents % i

print(f" {coins}")
