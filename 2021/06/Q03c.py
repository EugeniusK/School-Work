count = 0
theLine = ""

cities_file = open('Cities.txt', 'r')
numbered_file = open('Numbered.txt', 'w')

for city in cities_file.readlines():
    count = count + 1
    city_cleaned = city.replace('\n', '')
    theLine = f'{count} {city_cleaned}\n'
    print(theLine)
    numbered_file.write(theLine)
cities_file.close()
numbered_file.close()