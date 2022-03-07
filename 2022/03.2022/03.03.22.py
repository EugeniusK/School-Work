from tkinter import N


def taskOne():
    return -1

def taskTwo():
    def validate(question, type):
        valid = False
        while valid == False:
            user_answer = input(question)
            if type == str:
                if user_answer.isalnum:
                    return user_answer
            elif type == int:
                if user_answer.isnumeric:
                    return int(user_answer)
    class Ingredient:
        def __init__(self, name, quantity, units):
            self.name = name
            self.quantity = quantity
            self.units = units
        
        def recalculate(self, number_people, new_number_people):
            return f'{self.name} - {format(self.quantity / number_people * new_number_people, ".2f")}{self.units}'

    class Recipe:
        def __init__(self, recipe_name, number_people, list_of_ingredients):
            '''recipe_name --> str
            number_people --> int
            list_of_ingredients --> array of Ingredients(s)
            '''
            self.recipe_name = recipe_name
            self.number_people = number_people
            self.list_of_ingredients = list_of_ingredients
        
        def recalculate(self, new_number_people):
            print(f'Recipe - {self.recipe_name}')
            print(f'Number of people - {new_number_people}')
            for ingredient in self.list_of_ingredients:
                print(ingredient.recalculate(self.number_people, new_number_people))
        
                

    class RecipeBook:
        def __init__(self):
            self.recipe_book = []

        def new_recipe(self):
            name = validate('Please input the name of the recipe : ', str)
            people_served = validate('Please input the number of people served : ', int)
            end = False
            ingredients = []
            while end == False:
                ingredient_name = validate('Please input the name of the ingredient', str)
                ingredient_quantity = validate('Please input the quantity of the ingredient', int)
                ingredient_unit = validate('Please input the unit of the ingredient', int)
                ingredients.append(Ingredient(ingredient_name, ingredient_quantity, ingredient_unit)) 
                if input('END?').lower() == 'end':
                    end = True
            self.recipe_book.append(Recipe(name, people_served, ingredients))

        def display_all(self):
            for r in self.recipe_book:
                print(f'Recipe - {r.recipe_name}')
                print(f'Number of people - {r.number_people}')
                for i in r.list_of_ingredients:
                    f'{r.name} - {r.quantity}{r.units}'

    recipebook = RecipeBook
    while True:
        action = input('<VIEW RECIPES>, <ADD RECIPE>, <RECALCULATE RECIPE>')
        if action == 'ADD RECIPE':
            recipebook.new_recipe(recipebook)
        elif action == 'VIEW RECIPES':
            recipebook.display_all(recipebook)
        elif action == 'RECALCULATE RECIPE':
            valid = False
            while valid == False:
                user_input = input('INPUT RECIPE NAME')
                found = False
                for recipe in recipebook.recipe_book:
                    if recipe.recipe_name == user_input:
                        new_number_people = validate('INPUT NEW NUMBER OF PEOPLE', int)
                        recipe.recalculate(new_number_people)
                if found == False:
                    print('RECIPE NOT FOUND')
                    

def taskThree():
    return -1

taskTwo()