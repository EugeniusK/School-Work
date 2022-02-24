import math
#Q04

ships = [["Seabulk Pride",204184,390,50,2018],
        ["USS Sherman",61748,400,55,1992],
        ["MSC Carmen",220518,390,60,1993],
        ["MT Sidsel Knutsen",72774,398,57,1983],
        ["Salem",97105,397,54,1991],
        ["MCP Altona",42452,393,53,2005],
        ["MV Star Osakana",56210,396,55,1985],
        ["MSC Pamela",201985,400,59,1982],
        ["MSC Carouge",140758,400,60,1968],
        ["MV Southern Lily",178872,392,52,1977],
        ["MSC Sabrina",147799,394,52,1997],
        ["SS Fredericksburg",115460,392,50,2007],
        ["MV Sirius Star",113883,391,54,2012],
        ["MSC Nuria",201665,396,52,2007],
        ["MS Star Clipper",43364,394,51,1979],
        ["MSC Monterey",176953,397,53,1996],
        ["MSC Napoli",21953,400,55,1979],
        ["Shuttle tanker",194383,399,58,1967],
        ["MSC Geneva",183986,395,59,2015],
        ["MSC Rosaria",150530,394,54,1968],
        ["MSC Cordoba",63222,399,60,2002],
        ["MV Sea Empress",199487,392,56,2008],
        ["MSC Leigh",155215,400,60,1986],
        ["MV Sea Star",159402,398,58,1992],
        ["Sitakund",21887,394,57,1972]]

shipLabels = []   # Put the new labels into this structure

# ----------------------------------------------
# Write your code below this line

smallest = -1
smallest_name = ''
largest = 0
largest_name = ''
for ship in ships:
    name = ship[0]
    gross_tonnage = ship[1]
    length = ship[2]
    width = ship[3]
    YoM = ship[4]
    
    max_containers = math.floor(gross_tonnage / 2 / 30)
    useable_area = int(length * width / 2)
    label = f"{name} - Length : {length}m - Area : {useable_area}m^2 - Max containers : {max_containers} - Year : {YoM}"
    
    shipLabels.append(label)
    
    if max_containers > largest:
        largest = max_containers
        largest_name = name
    if smallest == -1:
        smallest = max_containers
        smallest_name = name
    elif max_containers < smallest:
        smallest = max_containers
        smallest_name = name

for label in shipLabels:
    print(label)
print(f"{smallest_name} could hold the least containers with only {smallest} being the limit")
print(f"{largest_name} could hold the least containers with {largest} containers being the limit")
