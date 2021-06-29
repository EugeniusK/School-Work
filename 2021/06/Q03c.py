#Do not use any oher data structure such as an array or list.
count = 0 #A counter for the line numbers
theLine = "" #Holds each line of the file

#Open "Cities.txt" as input
cities_file = open('Cities.txt', 'r')
#Open "Numbered.txt" as output
numbered_file = open('Numbered.txt', 'w')

#Use a for/each lioop to read each line of
#the input file into a variable named 'theline'
for city in cities_file.readlines():
    #increment the line count
    count = count + 1
    #Add the line umber to the front of the line followed by a space
    theLine = f'{count} {city}'
    #print the line to the display
    print(theLine)
    #write the new line to the output file
    numbered_file.write(theLine)

#close the input file
cities_file.close()
#close the output file
numbered_file.close()