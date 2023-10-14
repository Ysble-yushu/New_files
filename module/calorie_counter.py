calories = {
   'Hamburger': 600,
   'Cheese Burger': 750,
   'Veggie Burger': 400,
   'Vegan Burger': 350,
   'Sweet Potatoes': 230,
   'Salad': 15,
   'Iced Tea': 70,
   'Lemonade': 90,
}

combos = {
    "Cheesy Combo" : ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo" : ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo" : ["Vegan Burger", "Salad", "Lemonade"],
}

def get_full_name(first_name, last_name):
	return first_name + " " + last_name

def get_title_and_full_name(title, first_name, last_name):
	return title + " " + get_full_name(first_name, last_name)

full_name = get_title_and_full_name("Mr.", "Sam", "Onaisi")
print(full_name)

def meals(*args):
    total = 0
    for arg in args:
        for item in arg:
            try:
                if item in calories.keys():
                    total += calories[item]
                elif item in combos.keys():
                    for item in combos[item]:
                        total += calories[item]
                else:
                    print("Not in menu")
                    calories[item]
            except KeyError:
                print(f"KeyError: {item} not found in calories and combos")
    print(f"Total calories:{total}")
    return total