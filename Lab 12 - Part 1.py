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
    sentence = sentence.split()
    morse_sentence = []
    morse_word = []

    for i in range(len(sentence)):
        for letter in sentence[i]:
            if letter in morse_code_dict:
                morse_word.append(morse_code_dict[letter])
        morse_sentence.append(morse_word)
        morse_word = []

    return morse_sentence

def filter_sentence(user_sentence):
    user_sentence = user_sentence.lower()
    filtered_sentence = ''
    for char in user_sentence:
        if char in morse_code_dict:
            filtered_sentence += char
        elif char == ' ':
            filtered_sentence += ' '
    return filtered_sentence


while True:
    #Prompt user for a sentence
    user_input = input('Please enter a sentence: ')

    #Convert sentence to lower case and remove unwanted characters
    filtered_input = filter_sentence(user_input)

    #Convert the sentence to morse code
    morse_code_sentence = create_morse(filtered_input)
    print(morse_code_sentence)


