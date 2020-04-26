# put your python code here
duration = int(input())
food_cost_daily = int(input())
one_flight_cost = int(input())
hotel_night_cost = int(input())
print(duration * food_cost_daily + one_flight_cost * 2 + (duration - 1) * hotel_night_cost)