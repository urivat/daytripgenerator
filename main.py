destinations = ['Atlanta', 'Nashville', 'Tokyo', 'Sydney', 'The Moon' , 'Hawaii', 'New York', 'Miami' ]
restaurants = ['lumber jacks', "Lily's BBQ", 'Pho Cafe', 'four seasons', "hell's kitchen"]
Transportation = ['car', 'bullet train', 'slow train', 'horse and carriage', 'boat', 'spaceship', 'hotwheel']
entertainment = ['State park', 'izakaya', 'six flags', 'basketball game', 'explore the city', 'A japanese shrine','beachday','drive into a crater']

import random
def pick_a_destination(list_of_destinations):
    random_destination = random.choice(list_of_destinations)
    return random_destination
result_des = pick_a_destination(destinations)
print(f'Congratulations we have randomly selected your trip for today going to {result_des} is this ok? ')
selection = input('y/n ')
while selection == 'n':
    result_des = pick_a_destination(destinations)
    print(f'Congratulations we have randomly selected your trip for today going to {result_des} is this ok? ')
    selection = input('y/n ')
def pick_a_restaurant(list_of_restaurants):
    random_restaurant = random.choice(list_of_restaurants)
    return random_restaurant
results_rest = pick_a_restaurant(restaurants)
print(f'The restaurant choice is {results_rest} is this acceptable? ')
selection = input('y/n ')
while selection == 'n':
    results_rest= pick_a_restaurant(restaurants)
    print(f'The restaurant choice is {results_rest} is this acceptable? ')
    selection = input('y/n ')
def pick_a_mode_of_transport(list_of_transportation_options):
    random_transportation = random.choice(list_of_transportation_options)
    return random_transportation
type_of_vic = pick_a_mode_of_transport(Transportation)
print(f'Your mode of travel will be by {type_of_vic}')
selection = input('y/n ')
while selection == 'n':
   print(f'Your mode of travel will be by {type_of_vic}')  
   selection = input('y/n ')  
def pick_some_entertainment(list_of_fun):
    random_fun = random.choice(list_of_fun)
    return random_fun
types_of_fun = pick_some_entertainment(entertainment)
print(f'You will experience a day of fun at {types_of_fun} is this accptable? ')
selection = input('y/n ')
while selection == 'n':
    print(f'You will experience a day of fun at {types_of_fun} is this accptable? ')    
    selection = input('y/n ')
print('Congrats, your trip has been completely generated. Just to confirm this is your trip below')
def Confirmation_list():
    print(f'destination: {result_des}')
    print(f'restaurant: {results_rest}')
    print(f'travel type: {type_of_vic}')
    print(f'entertainment: {types_of_fun}')
Confirmation_list()
selection = input("everything look good for you? enter: y/n ")
if selection == 'n':
    print("sorry we couldnt help you're welcome to try again")
else:
    print('Perfect, glad we could help you with your decision! ')
print(f'Hope you are prepared for a wonderful trip. we have you arriving at {result_des} then having a nice lunch at {results_rest}. For the fun of the day you will travel by {type_of_vic} going around the area with a {types_of_fun}')
# (5 points): As a user, I want a destination to be randomly selected for my day trip.  
# from math import pi
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.  
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.  
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.  
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.  
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.  
# (5 points): As a developer, I want to make at least three commits with descriptive messages.  
# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists.  
# (10 points): As a user, I want to display my completed trip in the console.  
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing! 