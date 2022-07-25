cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}


def print_all_recipes():
    print("\n".join(cookbook.keys()))

def print_details(name: str):
    try:
        print(f"{name} ingredients are: " + " ".join(cookbook[name]["ingredients"]))
        print(f"{name} meal type is: " + cookbook[name]["meal"])
        print(f"{name} preparation time is:", cookbook[name]["prep_time"])
    except:
        print(f"{name} recipe doesn't exist") 

def delete_a_recipe(name: str):
    try:
        del cookbook[name]
    except:
        print(f"{name} recipe doesn't exist")

def add_a_recipe():
    ingredients = []
    meal_type = ""
    prep_time = 0

    name = input(">>> Enter a name:\n")

    while True:
        ingredient = input(">>> Enter ingredients:\n")
        if ingredient == "":
            break
        ingredients.append(ingredient)
    
    meal_type = input(">>> Enter a meal type:\n")
    
    while True:
        prep_time = input(">>> Enter preparation time:\n")
        try:
            prep_time = int(prep_time)
            break
        except:
            pass

    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal_type,
        "prep_time": prep_time,
    }

cookbook_functions = {
    1: add_a_recipe,
    2: delete_a_recipe,
    3: print_details,
    4: print_all_recipes,
    5: exit
}

def print_menu():
    print("List of available option:")
    print("    1: Add a recipe")
    print("    2: Delete a recipe")
    print("    3: Print a recipe")
    print("    4: Print the cookbook")
    print("    5: Quit")

def main():
    print("Welcome to the Python Cookbook !")
    print_menu()

    while True:
        option = input("\nPlease select an option:\n>> ")
        try:
            option = int(option)
        except:
            print("Invalid option.")
            print_menu()
            continue
        if 4 > option > 1:
            name = input("Please enter the name:\n>> ")
            cookbook_functions[option](name)
        else:
            cookbook_functions[option]()

if __name__ == '__main__':
    main()
