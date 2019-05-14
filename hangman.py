import random

# 6 tries
sentenceVault = [
'Banjo',
'Bungler',
'Croquet',
'Crypt',
'Dwarves',
'Fervid',
'Fjord',
'Gazebo',
'Haiku',
'Ivory',
'Jinx',
'Jukebox',
'Klutz'
]

guessesLeft = 6
userInput = ""
wrongLetters = []

def beginning():
	print('Welcome to hangman!')
	userChoice = input('Would you like to play?\n')

	if userChoice.lower() == 'yes':
		showWord(sentenceVault[random.randint(0, len(sentenceVault) -1)])
	elif userChoice.lower() == 'no':
		print('You quit')
		quit()
	else:
		print('Please enter yes or no\n')
		beginning()

def showWord(sentence):
	sentenceCopy = []
	for word in sentence:
		sentenceCopy.append('_');
	print(" ".join(sentenceCopy))
	userGuess(sentence, sentenceCopy);


def addLetterToCopy(sentence, sentenceCopy, userInput):
	letterIndex = sentence.lower().find(userInput)
	sentenceCopyList = list(sentenceCopy)
	letterIndexCopy = letterIndex if letterIndex -1 == -1 else letterIndex
	sentenceCopyList[letterIndexCopy] = sentence[letterIndex]

	if ("".join(sentenceCopyList) == sentence):
		print(f'\nThe word was: {sentence}')
		print('\nYOU WIN')
		quit()
	else:
		print(" ".join(sentenceCopyList))

	return sentenceCopyList

def userGuess(sentence, sentenceCopy, guessesLeft = guessesLeft, userInput = userInput, wrongLetters = wrongLetters):
	userInput = input(f'Guesses left: {guessesLeft}\nGuess a letter: ')
	check = checkIfCorrect(userInput, sentence)
	if check[1]:
		print('You guessed a letter!\n')
		sentenceCopy = addLetterToCopy(sentence, sentenceCopy, userInput[0])
		userGuess(sentence, sentenceCopy, guessesLeft)
	else:
		print('You guessed wrong\n')
		print(" ".join(sentenceCopy))
		wrongLetters.append(userInput)
		print(f'Wrong letters used: {" ".join(wrongLetters)}')
		guessesLeft -= 1
		if guessesLeft == 0:
			print('You lost')
			print(f'The word was: {sentence}')
			quit()
		userInput = ''
		userGuess(sentence, sentenceCopy, guessesLeft)



def checkIfCorrect(userInput, sentence):
	if len(userInput) > 1 or userInput.isnumeric():
		print('Please only enter a letter.\n')
		userGuess(sentence, sentenceCopy)

	for letter in sentence:
		if sentence.lower().find(userInput) < 0:
			return [userInput, False]
		else:
			return [userInput, True]




beginning()