# Exercise 1
# Rock Paper Scissors

from random import randint

print('Welcome to Rock, Paper, Scissors game! \n')



def rps_game():
	options = ['r', 'p', 's']

	for i in range(0,2):
		player = input('Plase type your choice: Rock(r), Paper (p) or Scissors(s) ? \n').lower()
		computer = options[randint(0,2)].lower()
		print("computer: {}".format(computer))
		if player == computer:
			print("Nobody wins! It's a tie!")
			while True:
				player = input('Plase type your choice: Rock(r), Paper (p) or Scissors(s) ? \n').lower()
				computer = options[randint(0,2)].lower()
		elif (player == 'r' and computer=='s') or (player == 's' and computer=='p') or (player == 'p' and computer=='r'):
			print("You won, computer lose!:)")
		else:
			print("You lose, computer won!:(")









