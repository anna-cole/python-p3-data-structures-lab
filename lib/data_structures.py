spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# Define a function get_names() that takes a list of spicy_foods and returns a list of strings with the names of each spicy food.
# You need to return the values ["Green Curry", "Buffalo Wings", "Mapo Tofu"]. To get the name value out of each food, you have to iterate over the foods and save them into a list. Retrieve the value with this syntax: food["name"]. 

def get_names(spicy_foods):
    spicy_list = [food["name"] for food in spicy_foods]
    return spicy_list

get_names(spicy_foods)


def get_spiciest_foods(spicy_foods):
    spicy_list = [food for food in spicy_foods if food["heat_level"] > 5]
    return spicy_list

get_spiciest_foods(spicy_foods)


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

#print_spicy_foods(spicy_foods)    


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food["cuisine"]:
            return food
    
get_spicy_food_by_cuisine(spicy_foods, 'American')


def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    return print_spicy_foods(spiciest_foods)

#print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    heat_levels = [food["heat_level"] for food in spicy_foods]
    average_heat_level = sum(heat_levels) / len(heat_levels)
    return average_heat_level
    
get_average_heat_level(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

create_spicy_food(spicy_foods, {'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10,})
