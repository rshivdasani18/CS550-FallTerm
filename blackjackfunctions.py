"""
Rohin Shivdasani
Fall Mini Final Project: Blackjack Game - one player competing against the dealer.
11/7/17
CS550 A Block, Ms. Healey
'On my honor I have neither given nor received unauthorized aid on this assignment.'
Sources:
https://www.youtube.com/watch?v=yJz2at4Hco4
https://codereview.stackexchange.com/questions/149889/simple-blackjack-game-in-python
https://codeboom.wordpress.com/2012/07/30/10-mini-programming-projects/
https://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list-python
https://stackoverflow.com/questions/26961427/asking-the-user-if-they-want-to-play-again
"""

import random


class deck:
	def __init__(self, size):
		self.size=52
		self.DECK = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,12,12,12,12,13,13,13,13,14,14,14,14]
		#In self.DECK, 1's represent aces, 12's represent Jacks, 13's represent Queens, and 14's represent Kings. Also, in this initial list, we will let ace be 11, but I am making it so that ace becomes a one if you bust.
	def deal(self):
		cardONE = random.randint(0, self.size-1)
		cardDEALT = self.DECK[cardONE]
		self.size -= 1
		del self.DECK[cardDEALT]
		return cardDEALT

def initialize():
	global playerhand
	global dealerhand
	global myDECK
	myDECK = deck(52)	

	playerhand.append(myDECK.deal())
	playerhand.append(myDECK.deal())
	dealerhand.append(myDECK.deal())
	dealerhand.append(myDECK.deal())


def ShowDealtCards():
	global dealerhandFACE
	global dic
	dic = {11:"A", 12:"J", 13:"Q", 14:"K"} #This dictionary is what I use to print the face cards as strings from their corresponding integer element values in the self.DECK list. I had to do this because the class and function did not work with strings an integers in the list. I got this idea from: https://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list-python

	print("\a")

	print("your hand:")
	playerhandFACE = [dic[n] if n in dic else n for n in playerhand] #This just executes the find and replacements that I defined in the above dictionary. I got this from the same website: https://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list-python
	print (playerhandFACE[0] , "," , playerhandFACE[1])

	print("\a")
	dealerhandFACE = [dic[n] if n in dic else n for n in dealerhand] #This just executes the find and replacements that I defined in the above dictionary. I got this from the same website: https://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list-python
	print("the dealer is showing:")
	print(dealerhandFACE[0])

	
def AskNextMove():
	print("")
	global hitORstay
	hitORstay = input("stay or hit? \a: ")
	hitORstay = hitORstay.lower().strip()
	while hitORstay != "stay" and hitORstay!= "hit":
		print("error. type hit or stay.")
		hitORstay = input("stay or hit? \a: ")
	


def HIT():
	global hitORstay
	while hitORstay == "hit":
		playerhand.append(myDECK.deal())
		playerhandFACE = [dic[n] if n in dic else n for n in playerhand]
		print("\a")
		print ("your hand: ", end='')
		print(*playerhandFACE, sep=', ') 
		print("\a")

		dicTENS = {12:10, 13:10, 14:10}
		check = [dicTENS[n] if n in dic else n for n in playerhand]
		if sum(check)>21:
			if check[0] or check[1] == 11: #this if statement first checks if you have any aces(11's) and converts them into 1's so that you don't bust since an ace can be either a 1 or 11 in blackjack.
				dicACE = {11:1} #this turns all aces in the hand into 1's, but if you have 2 aces, then you might not want to convert both. How do I rectify this???
				check = [dicACE[n] if n in dic else n for n in check]
			if sum(check)>21:
				break

		hitORstay = input("stay or hit? \a: ")
		hitORstay = hitORstay.lower().strip()



def STAY():
	global playerhand
	global dealerhand
	#if hitORstay == "stay": #once the player is content with their hand, their hand is calculated here and then compared with that of the dealer. Then the result of the round is displayed.
	dic = {12:10, 13:10, 14:10} #converts self.DECK's jack,queen,king placeholder's into thier correct numerical value of 10 so that we can do the addition of the hands.
	playerhand = [dic[n] if n in dic else n for n in playerhand]
	dealerhand = [dic[n] if n in dic else n for n in dealerhand]


	playersum = sum(playerhand)
	dealersum = sum(dealerhand)

	if playersum > 21:
		if playerhand[0] or playerhand[1] == 11: #this if statement first checks if you have any aces(11's) and converts them into 1's so that you don't bust since an ace can be either a 1 or 11 in blackjack.
			dic = {11:1}
			playerhand = [dic[n] if n in dic else n for n in playerhand]

	playersum = sum(playerhand) #now recalculate the sum of the player's cards

	# if hitORstay == "stay":
	# 	print("\a")
	if playersum > 21:
		print("BUST! You Lose.")
	elif playersum == dealersum:
		print("push (tie).")
	elif playersum == 21:
		print("BLACKJACK! $$$$$ You Win!")
	elif playersum > dealersum:
		print("You Win!")
	elif playersum < dealersum:
		print("You Lose.")
	

	print("\a")
	print("The dealer's hand was:" , dealerhandFACE[0] , "," , dealerhandFACE[1])
	print("\a")





hitORstay = ''
dealerhandFACE = ''
playerhand = []
dealerhand = []
myDECK = deck(52)
play = True

start = False
while start ==False:
	print("\a")
	print("Blackjack instructions: you will be dealt a hand of two cards. The dealer will be dealt two cards as well, but you can only see one of his cards. The goal is to get your hand closer to 21 than the dealer's hand without going over 21. Ace is 11 or 1, and King, Queen, and Jack are 10. You may ask for additional cards by 'hitting'. If you haven't busted, type 'stay' once you are satisfied with your hand.")
	print("\a")
	start = True


while play:
	initialize()

	ShowDealtCards()

	AskNextMove()

	HIT()

	STAY()

	again = input("Play Again?: ")
	again = again.lower().strip()

	if again != "yes":
		play = False
	else:
		play = True
		playerhand = []
		dealerhand = []



















"""
Here is what I wrote out and my initial thinking about how to approach
the game before I started writing any code. As I started coding, I changed 
things, especially when I came in for extra help, but I just included this 
in case you might want to see.


Outline, objectives, and planning:

	-object: deck of cards

	-function: Deal cards out (don't care about suit in blackjack, only number)

	-object: Dealer's cards (gets 2 cards) #can these just stay as lists outside of any class?
	-object: Player's cards (gets 2 cards) #can these just stay as lists outside of any class?

	-function: Display the cards (only one of the dealer's cards, but both of the player's cards)

	-function: Sum of the Dealer's cards
	-function: Sum of the Player's cards
	
	-function: Compare the Dealer's sum to the Player's sum.
		-If Player's sum > 21, BUST
			-Player LOSES
		-If Player's sum > 21, option to HIT or STAY
			-If option = STAY, compare the Dealer's sum to the Player's sum.
				-If Player's sum <= 21 && > Dealer's sum, Player WINS
				-If Player's sum < Dealer's sum, Player LOSES.
			-If option = HIT
				-make a hit function and call it (just one iteration of the deal function)
				-then call the compare function and loop back to hit function if needed.
"""










