# Q03

#	Open the files and input data
file_names = open("File names.txt", "r")
file_names_array = file_names.readlines()

#	Open output file
audio_files = open("Audio files.txt", "w")

#	Identify audio files and add to new file
for filename in file_names_array:
    if '.mp3' in filename:
        audio_files.write(filename)
    elif 'flac' in filename:
        audio_files.write(filename)
    elif 'wma' in filename:
        audio_files.write(filename)

#	Close files
file_names.close()
audio_files.close()