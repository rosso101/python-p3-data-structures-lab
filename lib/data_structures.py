spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    nameList = []
    for curly in spicy_foods:
        nameList.append(curly.get("name"))
    return nameList  


ddef print_spicy_foods(spicy_foods):
    for foods in spicy_foods:
        heat_level = "🌶" * foods.get("heat_level")
        print(f"{foods.get('name')} ({foods.get('cuisine')}) | Heat Level: {heat_level}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
     for foods in spicy_foods:
         if foods.get("cuisine") == cuisine:
             return foods
    

def print_spiciest_foods(spicy_foods):
    spicingFoods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spicingFoods)
   
def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    for food in spicy_foods:
        total_heat_level += food.get("heat_level")
    if len(spicy_foods) > 0:
        average_heat_level = total_heat_level / len(spicy_foods)
        return average_heat_level
    

def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods
