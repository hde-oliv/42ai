from datetime import datetime
from book import Book
from recipe import Recipe

def first_test():
    a_book = Book("Energetics")

    a_book.add_recipe(Recipe("Red Bull", 4, 50, ["Taurine", "Caffeine"], "dessert"))
    a_book.add_recipe(Recipe("Green Bull", 3, 40, ["Taurine", "Caffeine"], "dessert"))
    a_book.add_recipe(Recipe("Blue Bull", 9, 80, ["Taurine", "Caffeine"], "dessert"))

    a_book.get_recipe_by_name("Red Bull")
    a_book.get_recipe_by_name("Green Bull")
    a_book.get_recipe_by_name("Blue Bull")

    listy = a_book.get_recipes_by_type("dessert")
    print(*listy)


def main():
    first_test()


if __name__ == '__main__':
    main()

