import random


def create_word_hint(word, hidden):
    index = 0
    word_hint = ''
    while index < len(word):
        if hidden[index]:
            word_hint += word[index]
        else:
            word_hint += '-'
        index += 1
    return word_hint


def gen_word():
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    return word


def gen_hidden(word):
    hidden = []
    for _ in word:
        hidden.append(False)
    return hidden


def change_hidden(word, hidden, letter):
    index = 0
    while index < len(word):
        if letter == word[index]:
            hidden[index] = True
        index += 1


def play():
    magic_word = gen_word()
    open_letters = gen_hidden(magic_word)
    word_set = set(magic_word)
    guessed_letters = ''

    tries = 8
    guesses = 0
    while guesses < tries:
        hidden_word = create_word_hint(magic_word, open_letters)
        print()
        print(hidden_word)
        if hidden_word == magic_word:
            print('You guessed the word!')
            print('You survived!')
            break
        guess = input('Input a letter: ')
        if guess in guessed_letters:
            print('You already typed this letter')
        elif len(guess) > 1:
            print('You should input a single letter')
        elif not (guess.isalpha() and guess.islower()):
            print('It is not an ASCII lowercase letter ')
        elif guess not in word_set:
            print('No such letter in the word')
            guessed_letters += guess
            guesses += 1
        else:
            change_hidden(magic_word, open_letters, guess)
            guessed_letters += guess
    else:
        print('You are hanged!')
        print()


def menu():
    print('H A N G M A N')
    choice = ''
    while choice != 'exit' and choice != 'play':
        choice = input('Type "play" to play the game, "exit" to quit: ')
        if choice == 'exit':
            break
        if choice == 'play':
            play()


menu()
