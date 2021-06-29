theArtists = [
    ['Andy', 'Warhol', 1928],
    ['Pablo', 'Picasso', 1881],
    ['Salvador', 'Dali', 1904],
    ['Lavinia', 'Fontana', 1552],
    ['Jackson', 'Pollock', 1912],
    ['Henri', 'Matisse', 1869],
    ['Frida', 'Kahlo', 1907],
    ['Georgeia', "O'Keeffe", 1887],
    ['Kara', 'Walker', 1969],
    ['Yayoi', 'Kusama', 1929]
]

theLabels = []

for artist in theArtists:
    surname_letter = artist[1][0]
    forename_letter = artist[0][0]
    year = artist[2]
    label = f'{surname_letter}{forename_letter}{year}'
    theLabels.append(label)

print(theLabels)

youngest_artist_age = 0
younget_artist = []
for artist in theArtists:
    artist_year = artist[2]
    if artist_year > youngest_artist_age:
        youngest_artist_age = artist[2]
        youngest_artist = artist

print(youngest_artist)