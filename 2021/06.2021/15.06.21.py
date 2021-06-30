#uses File names.txt
file_names = open("File names.txt", "r")
file_names_array = file_names.readlines()
audio_file = open("Audio files.txt", "w")

for filename in file_names_array:
    if '.mp3' in filename:
        audio_file.write(filename)
    elif 'flac' in filename:
        audio_file.write(filename)
    elif 'wma' in filename:
        audio_file.write(filename)

audio_file.close()