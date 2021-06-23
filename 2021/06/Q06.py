theArtists = [
    ['Andy', 'Warhol', 1928],
    ['Pablo', 'Picasso', 1881],
    ['Salvador', 'Dali', 1904]
]

theLabels = []

for artist in theArtists:
    surname_letter = artist[1][0]
    forename_letter = artist[0][0]
    year = artist[2]
    label = f'{surname_letter}{forename_letter}{year}'
    theLabels.append(label)

print(theLabels)

print(sorted(theArtists, key=lambda x:x[2])[0])