# Q04

#	Open the files and input data
alice_file = open('Alice.txt', 'r')
alice_lines = alice_file.readlines()

#	Open output file
think_file = open('think.txt', 'w')

#	Perform analysis

alice_count = 0
for line in alice_lines:
    if 'think' in line:
        think_file.write(line)
    if 'Alice' in line:
        alice_count = alice_count + 1

print(alice_count)

#   Close files
alice_file.close()
think_file.close()
