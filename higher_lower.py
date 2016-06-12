#import libraries go here
import random

#global variables go here
_gameOn = None
_guesses = None
_secret = None

#function for easy version
def DifficultyLevelEasy():
	global _secret
	_secret = int(random.randrange(0, 100))
	print ('Press Q to exit')
	while _gameOn:
		guessStr = input('Guess a number')		
		if guessStr == 'Q':
			print('Our secret: ' + str(_secret))
			PlayAgain()
			break
		guess = int(guessStr)
		if guess > _secret:
			print('your guess is too high. Try again')
		elif guess < _secret:
			print('your guess is too low. Try again')
		elif guess == _secret:
			print('You win!')
			PlayAgain()
		


#function for hard version
def DifficultyLevelHard():
	global _guesses 
	global _secret
	_guesses = 3
	_secret = int(random.randrange(0, 100))
	for i in range(_guesses):
		guess = int(input('Guess a number:'))
		if i == _guesses - 1:
			print('GameOver')
			print('Our secret: ' + str(_secret))
			PlayAgain()
			break
						
		elif guess > _secret:
			print('your guess is too high. Try again')
		elif guess < _secret:
			print('your guess is too low. Try again')
		elif guess == _secret:
			print('You win!')
			PlayAgain()
		
		
	
	

#function to start game
def StartGame():
	global _gameOn
	_gameOn = True
	level = input('Welcome. Type easy(1), hard(2) or quit(others)')
	if level == '1':
		DifficultyLevelEasy()
	elif level == '2':
		DifficultyLevelHard()
	else:
		StopGame()


#function to stop game
def StopGame():
	global _gameOn
	_gameOn = False
	print("Goodbye!")

def PlayAgain():
	play = int(input('Play again? Yes(1) No(0)'))
	if play == 1:
		StartGame()
	elif play == 0:
		StopGame()

#function calls go here
StartGame()