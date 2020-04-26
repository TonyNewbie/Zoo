# put your python code here
first_hours = int(input())
first_minutes = int(input())
first_seconds = int(input())
second_hours = int(input())
second_minutes = int(input())
second_seconds = int(input())
print((second_hours - first_hours) * 3600 + (second_minutes - first_minutes) * 60 + second_seconds - first_seconds)
