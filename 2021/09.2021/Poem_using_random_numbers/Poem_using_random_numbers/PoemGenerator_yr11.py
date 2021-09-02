#arrays and randomness

#random library allows us to generate random numbers
import random
import easygui
#first part can be any of these words

    
part1 = ['Tears', 'Fear', 'Happiness', 'Life', 'Computing', 'Python', 'British school in Tokyo']

#second part is chosen between any of these parts
part2 = ['like a', 'for the', 'near the', 'against a', 'where my secret lies as', 'is the focus of life as', 'that touched my']

#third part is chosen between any of these words
part3 = ['great', 'dying', 'extreme', 'deadly']

#second part is chosen between any of these parts
part4 = ['Nina', 'Richard', 'Python', 'dog', 'death']

#randomly decide the first part
rand1 = random.randint(0, len(part1) -1)
#randomly decide the second part
rand2 = random.randint(0, len(part2) -1)
#randomly decide the third part
rand3 = random.randint(0, len(part3) -1)
#randomly decide the last part
rand4 = random.randint(0, len(part4) -1)

# display a message explaining what the program does and include an image
message=easygui.msgbox("By pressing OK below, you will generate a deep, meaningful poem....", image="poem.gif")

#add together the random array elements
poem = easygui.msgbox(part1[rand1] + ", " + part2[rand2] + " " + part3[rand3] + " " + part4[rand4],"this is the poem that you have made", image="thought.gif")



