deposit = int(input())
protection_limit = 700000
percent = 0.071
years = 0
while deposit <= protection_limit:
    deposit += deposit * percent
    years += 1
print(years)
