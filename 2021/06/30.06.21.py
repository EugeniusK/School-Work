import time
#morse code
char_to_morse = {
    ' ' : '/',
    'A' : '.-',
    'B' : '-...',
    'C' : '-.-.',
    'D' : '-..',
    'E' : '.',
    'F' : '..-.',
    'G' : '--.',
    'H' : '....',
    'I' : '..',
    'J' : '.---',
    'K' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' : '.--.',
    'Q' : '--.-',
    'R' : '.-.',
    'S' : '...',
    'T' : '-',
    'U' : '..-',
    'V' : '...-',
    'W' : '.--',
    'X' : '-..-',
    'Y' : '-.--',
    'Z' : '--..',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    '0' : '-----',
}
char_list = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
morse_list = [' / ', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']
def string_to_morse(string):
    return ' '.join([morse_list[char_list.index(chr.upper())] for chr in string if chr.upper() in char_list])

def morse_to_string(morse):
    return ' '.join([''.join([char_list[morse_list.index(morse_chr)] for morse_chr in morse_word.split(' ') if morse_chr in morse_list]) for morse_word in morse.split(' / ')])

def section_one():
    input_sentence = input('Please enter a sentence\n')
    output_sentence = string_to_morse(input_sentence)
    print(f'Your sentence in morse code is\n{output_sentence}')

def section_two():
    selection = int(input('Press 1 to convert from English to Morse or 2 to convert from Morse to English'))
    if selection == 1:
        input_sentence = input('Please enter a sentence\n')
        output_sentence = string_to_morse(input_sentence)
        print(f'Your sentence in morse code is\n{output_sentence}')
    elif selection == 2:
        input_sentence = input('Please enter your Morse Code. You should leave a space between each letter and put a slash between words\n')
        output_sentence = morse_to_string(input_sentence)
        print(f'Your sentence in English is\n{output_sentence}')
    else:
        section_two()

def section_three():
    filename = input('Which file do you want to translate from or to Morse Code?\n')
    try:
        translate_file = open(filename, 'r')
        output_file = open('output.txt', 'w')
    except:
        print('This file does not exist')
        exit()
    
    selection = int(input('Press 1 to convert from English to Morse or 2 to convert from Morse to English'))
    if selection == 1:
        for line in translate_file.readlines():
            output_file.write(string_to_morse(line))
    elif selection == 2:
        for line in translate_file.readlines():
            output_file.write(morse_to_string(line))
    else:
        section_three()
    