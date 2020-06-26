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

def main():
    print('H A N G M A N')
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
            print('No improvements')
            guesses += 1
        elif guess not in word_set:
            print('No such letter in the word')
            guesses += 1
        else:
            guessed_letters += guess
            change_hidden(magic_word, open_letters, guess)
    else:
        print('You are hanged!')


main()
