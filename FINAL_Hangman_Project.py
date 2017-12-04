"""
Rohin Shivdasani
10/5/17
Project: Hangman
Sources:
	Lam Tran Bach (East Cottage) (test played my game and read over my code to error check.)
	Spencer Buebel (Carrboro High School) (talked with on phone to learn about append function.)

	websites used:
		http://www.thegeekstuff.com/2013/06/python-list/?utm_source=feedly
		https://www.tutorialspoint.com/python/python_lists.htm
		https://developers.google.com/edu/python/lists
		https://www.youtube.com/watch?v=zbVNGA1YuYw
		https://www.youtube.com/watch?v=9vul6XLtyB8
		https://www.youtube.com/watch?v=HO55hyX8EGM

Honor Code: On my honor, I have niether given nor received unauthorized aid
"""

import random
import string

words = ['basketball', 'octopus', 'sprint', 'chair', 'rollercoaster', 'engine', 'muscle']

# holds all the letters
remainingLetters = []

# if index value is 1, then letter hasn't been guessed, if 0, then letter has been guessed
remainingStatus = []

keepitgoing = True
while keepitgoing == True:

	# pick the game word
	i = random.randint(0, len(words)-1)
	gameWord = words[i]
	#print(gameWord) #debugging
	wordLength = len(gameWord)

	# keep track of guesses
	guessStatus = []
	for i in range(0, wordLength):
		guessStatus.append(0)

	# fill in remainingLetters
	for i in range(0, 26):
		remainingStatus.append(int(1))
		remainingLetters.append(string.ascii_lowercase[i])


	# Game has started
	playHangman = input("Do you want to play hangman? (y/n)): ")

	inGame = True

	while playHangman != 'y':
		if playHangman == 'n':
			print("It's fine... I didn't want to play either.\n")
			playHangman = input("Do you want to play hangman? (y/n)): ")
		elif playHangman != 'y':
			print("Something went wrong. Please type y or n.\n")
			playHangman = input("Do you want to play hangman? (y/n)): ")
			
		else:
			inGame = True


	# keep track of how many wrong guesses have been made
	strikes = 0

	# gameplay occurs here
	while inGame == True:

		# get user's guess
		guess = input("Guess a letter: ")
		print("\n\n")

		# add this to list of guessed letters (make its index 0)
		remainingStatusIndex = 0

		# basically just find which letter was guessed
		for i in range(0, 26):
			if guess == remainingLetters[i]:
				remainingStatusIndex = i
				i = 27
		remainingStatus[remainingStatusIndex] = 0

		# see if this guess is in the word
		wordIterator = 0
		correctGuess = False
		win = True
		for char in gameWord:
			if char == guess:
				# if so, then print this out
				correctGuess = True
				guessStatus[wordIterator] = 1
			if guessStatus[wordIterator] == 0:
				# if not, then print a void
				print("_"),
				win = False
			else:
				print(char),
			wordIterator += 1
		# if not, give user a strike
		if (correctGuess == False):
			strikes += 1

		print('\n')


		if (strikes==0):
			print(
			    '_____\n'
		        ' |   |\n'
		        '     |\n'
		       '     |\n'
		       '     |\n'
		             '     |\n'
		              )

		if (strikes==1):
			print(
			    ' ____\n'
		        ' |   |\n'
		        ' O   |\n'
		       '     |\n'
		       '     |\n'
		             '     |\n'
		              )

		if (strikes==2):
			print(
			    ' ____\n'
		        ' |   |\n'
		        ' O   |\n'
		       ' |   |\n'
		       '     |\n'
		             '     |\n'
		              )

		if (strikes==3):
			print(
			    ' ____\n'
		        ' |   |\n'
		        ' O   |\n'
		       '-|   |\n'
		       '     |\n'
		             '     |\n'
		              )

		if (strikes==4):
			print(
			    ' ____\n'
		        ' |   |\n'
		        ' O   |\n'
		       '-|-  |\n'
		       '     |\n'
		             '     |\n'
		              )

		if (strikes==5):
				print(
			    ' ____\n'
		        ' |   |\n'
		        ' O   |\n'
		       '-|-  |\n'
		       '/    |\n'
		             '     |\n'
		              )

		if (strikes==6):
			print(
			    ' ____\n'
		        ' |   |\n'
		        ' O   |\n'
		       '-|-  |\n'
		       '/ \\  |\n'
		             '     |\n'
		              )

		# Can change the number of strikes needed to lose here if necesarry
		if (strikes > 5):
			print("\n You lose. Try again if you want...")
			inGame = False
			
		# detect a win (if no more voids are present)
		if (win == True):
			print("\n You WON!")
			inGame = False
			
		print("\n")


		keepitgoing = True