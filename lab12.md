# Lab 12

1. Implement the morse code as a python dictionary. Only code the character and numbers present in the picture posted on Github.
2. On your laptop:
   1. Create a python program that:
      1. prompts the user for a sentence.
      2. convert the sentence to lowecase and remove any character/number without a morse code equivalent.
      3. Create a list that represents the morse code equivalent of the input sentence. Make sure you find a way to identify the end of a word in the list. Note: the space between parts of the same letter is one unit, the space between characters is three units and the space between words is seven units.
      4. Create as many functions as you need to make your code modular and portable.
3. On the Circuit Playground:
   1. Modify your code so that:
      1. It prompts the user for the length of a unit (between 0 and 1s), the unit is used as the time to wait between parts of a morse code letter, characters and words.
      2. It prompts the user for a sentence.
      3. It filters the sentence to make it lowercase and to remove unwanted characters.
      4. It creates the morse code equivalent as a list.
      5. It displays the morse code on the CP express using all ten leds lit in the color of your choice.