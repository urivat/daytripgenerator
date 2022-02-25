# (5 points): As a developer, I want to make at least three commits with descriptive messages.  

# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists.  
destinations = ['Atlanta', 'Nashville', 'Tokyo', 'Sydney', 'The Moon' , 'Hawaii', 'New York', 'Miami' ]
restaurants = ['lumber jacks', "Lily's BBQ", 'Pho Cafe', 'four seasons', "hell's kitchen"]
Transportation = ['car', 'bullet train', 'slow train', 'horse and carriage', 'boat', 'spaceship', 'hotwheel']
entertainment = ['State park', 'izakaya', 'six flags', 'basketball game', 'explore the city', 'A japanese shrine','beachday','drive into a crater']


# (5 points): As a user, I want a destination to be randomly selected for my day trip.  
# from math import pi
import random
def pick_a_destination(list_of_destinations):
    random_destination = random.choice(spots)
    return random_destination
spots = destinations
results = pick_a_destination(spots)
print(f'Congratulations we have randomly selected your trip for today going to {results} is this ok? ')

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.  
def pick_a_restaurant(list_of_restaurants):
    random_restaurant = random.choice(eats)
    return random_restaurant
eats = restaurants
results_rest = pick_a_restaurant(eats)
print(f'The restaurant choice is {results_rest} is this acceptable? ')

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.  
def pick_a_mode_of_transport(list_of_transportation_options):
    random_transportation = random.choice(vehicles)
    return random_transportation
vehicles= Transportation
type_of_vic = pick_a_mode_of_transport(vehicles)
print(f'Your mode of travel will be by {type_of_vic}')

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.  
def pick_some_entertainment(list_of_fun):
    random_fun = random.choice(fun)
    return random_fun
fun = entertainment
types_of_fun = pick_some_entertainment(fun)
print(f'You will experience a day of fun at {types_of_fun} is this accptable')

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.  
# this below function is responsible for reselecting list results
def random_reselect():
    user_pick = input('is this acceptable? enter: y/n ')
    while user_pick != 'y':
        print(f'sorry, you dont like that option what about   enter y/n')

      
user_select= 'answer'    
focus = random_reselect()
print(focus)



# question = input()    
# the_result = yey_or_nay
# print(the_result)
    

# print('perfect, lets move on')
    




    

# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.  

# (10 points): As a user, I want to display my completed trip in the console.  

# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing! 