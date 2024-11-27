import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.1
cp.pixels.auto_write = False

morse_code_dict = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}

def create_morse (sentence):
    """ Convert the sentence to morse code """
    sentence = sentence.split()
    morse_sentence = []
    morse_word = []

    for i in range(len(sentence)):
        for letter in sentence[i]:
            #if the letter is in the dictionary, append its morse code to the list morse_word
            if letter in morse_code_dict:
                morse_word.append(morse_code_dict[letter])
        #append the complete word to the morse_sentence list
        morse_sentence.append(morse_word)
        #empty the morse_word list for the next word
        morse_word = []

    return morse_sentence

def filter_sentence (user_sentence):
    """
    Change the sentence to all lower case and
    remove all characters that aren't in the dictionary.
    Keep the spaces to mark the end of a word.
    """

    user_sentence = user_sentence.lower()
    filtered_sentence = ''
    for char in user_sentence:
        if char in morse_code_dict:
            filtered_sentence += char
        elif char == ' ':
            filtered_sentence += ' '
    return filtered_sentence

def flash_lights (morse, ms):
    """ Take the morse code and flash the LEDs correspondingly """
    #determine the different values of wait time
    one_unit = ms
    three_units = ms * 3
    seven_units = ms * 7

    for word_index, word in enumerate(morse):
        for letter_index, letter in enumerate(word):
            for part_index, part in enumerate(letter):
                #if the part of the letter is a dot:
                if part == '.':
                    #flash for one unit, then turn off the LEDs
                    cp.pixels.fill((255, 255, 51))
                    cp.pixels.show()
                    time.sleep(one_unit)
                    cp.pixels.fill((0,0,0))
                    cp.pixels.show()
                #if the part of the letter is a dash:
                elif part == '-':
                    #flash for three units, then turn off the LEDs
                    cp.pixels.fill((255, 255, 51))
                    cp.pixels.show()
                    time.sleep(three_units)
                    cp.pixels.fill((0,0,0))
                    cp.pixels.show()
                #if there's another dot/dash in the letter, wait one unit
                if part_index != len(letter) - 1:
                    print(one_unit)
                    time.sleep(one_unit)
            #if there's another letter in the word, wait three units
            if letter_index != len(word) - 1:
                    print(three_units)
                    time.sleep(three_units)
        #if there's another word in the sentence, wait 7 units
        if word_index != len(morse) - 1:
                print(seven_units)
                time.sleep(seven_units)
    return

while True:
    try:
        #Prompt the user to enter a value in milliseconds
        unit = float(input('Please enter a unit of time in milliseconds, between 0 and 1: '))

        #if the value isn't between 0 and 1, ask the user to input another value
        if unit < 0 or unit > 1:
            print('\nPlease enter a number between 0 and 1\n')
            continue

        # Prompt user for a sentence
        user_input = input('Please enter a sentence: ')

        # Convert sentence to lower case and remove unwanted characters
        filtered_input = filter_sentence(user_input)

        # Convert the sentence to morse code
        morse_code_sentence = create_morse(filtered_input)

        #Flash the LEDs on the circuit playground to match the morse code
        flash_lights(morse_code_sentence, unit)

        #Prompt the user to start again or exit the program
        end = input('\nPress any key to continue, type \'exit\' to end the program: ')
        if end.lower() == 'exit':
            break
        else:
            continue

    except ValueError:
        print('\nPlease enter a valid number.\nExample: 0.7\n')
