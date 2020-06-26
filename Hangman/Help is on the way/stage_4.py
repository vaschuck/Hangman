import random
print('H A N G M A N')
print('The game will be available soon.')

words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
word_hint = word[:3] + '-' * (len(word) - 3)
guess = input('Guess the word ' + word_hint + ': ')

if word == guess:
    print('You survived!')
else:
    print('You are hanged!')
