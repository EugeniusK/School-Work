#Q02

theAnimals = [["Cat", 13, 46],
              ["Dog", 14, 64],
              ["Goldfish", 4, 5],
              ["Hamster", 3, 10],
              ["Mouse", 2, 15],
              ["Flea", 0.5, 0.01],
              ["Gerbil", 2, 7],
              ["Chinchilla", 7, 23],
              ["Guinea Pig", 8 ,19],
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

#output each animal's statistics
for animal in theAnimals:
    label = f"a {animal[0].lower()} lives until approximately {animal[1]} years and is {animal[2]}cm in length"
    theLabels.append(label)
    print(label)

#output average life expectancy
ageAnimals = [animal[1] for animal in theAnimals]
noAnimals = len(theAnimals)
print(f"the average life expectancy of the animals are {round(sum(ageAnimals)/noAnimals,1)} years")

#output name of the largest animal
largestAnimalSize = max([animal[2] for animal in theAnimals])
largestAnimalIndex = [animal[2] for animal in theAnimals].index(largestAnimalSize)
print(f"the name of the largest animal is a {theAnimals[largestAnimalIndex][0]}")

#output name of the smallest animal
smallestAnimalSize = min([animal[2] for animal in theAnimals])
smallestAnimalIndex = [animal[2] for animal in theAnimals].index(smallestAnimalSize)
print(f"the name of the smallest animal is a {theAnimals[smallestAnimalIndex][0]}")

#codename of animals
for animal in theAnimals:
    codename = animal[0][0:2]+str(animal[2])
    code.append(codename)
print(code)
#Q03

cameras = [["Sony Compact",10300,2016],
            ["Nikon Compact",10500,2017],
            ["Canon Compact",11200,2015],
            ["Lumix Compact",10000,2020],
            ["Polaroid Compact",9500,2019],
            ["Sony DSLR",67000,2014],
            ["Nikon DSLR",35000,2015],
            ["Canon DSLR",47500,2019]]

theLabels = []   # Put the new camera label into this structure

# ----------------------------------------------
# Write your code below this line
#generate a label for each camera
for camera in cameras:
    label = f"{camera[0]} - {camera[1]} yen - from {camera[2]}"
    theLabels.append(label)

#output the list of labels
print(theLabels)

#find the cheapest camera and output its label
cheapestCameraCost = min([camera[1] for camera in cameras])
cheapestCameraIndex = [camera[1] for camera in cameras].index(cheapestCameraCost)
print(f"the cheapest camera is {cameras[cheapestCameraIndex][0]} and it costs {cameras[cheapestCameraIndex][1]} yen")

#find the newest camera and output its label
newestCameraCost = max([camera[2] for camera in cameras])
newestCameraIndex = [camera[2] for camera in cameras].index(newestCameraCost)
print(f"the newest camera is {cameras[newestCameraIndex][0]} and it costs {cameras[newestCameraIndex][1]} yen")