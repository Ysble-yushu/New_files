import json
with open("data/data.json") as file:
    data = json.load(file)
    meals = data.get('meals', {})
    combos = data.get('combos', {})



def calories_counter(*items):
    total = 0
    for item in items:
        if item in meals.keys():
            total += meals[item]
        elif item in combos.keys():
            total += combos[item]
        else:
            print(f"{item} not in menu")
    return total

def price_calorie_counter(*items):
    total = 0
    for item in items:
        if item in meals.keys():
            total += meals[item]
        elif item in combos.keys():
           total += combos[item]
        else:
            print(f"{item} is not in the menu")
    return total

