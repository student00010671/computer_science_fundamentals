def letter_counter(word, character, index):
    amount = 0
    while index < len(word):
        if word[index] == character:
            amount += 1
        index += 1
    print("Character \"" + character + "\" appeared " + str(amount) + " time(s)!")


# 1st argument define the word itself, 2nd the character, and 3rd where to start looping
letter_counter("banana", "a", 0)
