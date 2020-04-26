atoms = int(input())
result_quantity = int(input())
days = 0
while atoms >= result_quantity:
    days += 12
    atoms //= 2
print(days)