#Q02

theAnimals = [["Cat", 13, 46],
              ["Dog", 14, 64],
              ["Goldfish", 4, 5],
              ["Hamster", 3, 10],
              ["Mouse", 2, 15],
              ["Flea", 0.5, 0.01],
              ["Gerbil", 2, 7],
              ["Chinchilla", 7, 23],
              ["Guinea Pig", 8, 19],
              ["Dolphin", 35, 210],
              ["Python", 40, 420],
              ["Bearded Dragon", 54, 52],
              ["Tarantula", 13, 17],
              ["Parrot", 80, 42],
              ["Parakeet", 75, 35],
              ["Budgie", 52, 14],
              ["Hedgehog", 5, 21],             
             ]

theLabels = []   # Put the new animal label into this structure
code=[]    #create the code names for each animal in here
# ----------------------------------------------
# Write your code below this line
total_life_expectancy = 0

largest_name = ""
largest_size = 0

smallest_name = ""
smallest_size = -1

for animal in theAnimals:
    print("a " + str(animal[0]) + " lives until approximately " + str(animal[1]) + " years and is " + str(animal[2]) + "cm in length")

    total_life_expectancy += animal[1]

    if animal[2] > largest_size:
        largest_name = animal[0]
        largest_size = animal[2]
    else:
        if smallest_size == -1 or animal[2] < smallest_size:
            smallest_name = animal[0]
            smallest_size = animal[2]

    code_name = animal[0][0:2] + str(animal[2])
    code.append(code_name)

print("The average expectancy of all animals is " + str(total_life_expectancy / len(theAnimals)) + " years")
print("The largest animal is a " + largest_name)
print("The smallest animal is a " + smallest_name)
for codename in code:
    print(codename)