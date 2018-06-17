
import random

max = 6
min = 1

def dice():
	return random.randint(min,max)

	
def game():
	while(1):
		print('Please input your guess of the dice (1~6), -1 to end the game:')
		guess=int (input());
		if (guess == -1):
			break
		else:
			now_dice=dice()
			if(guess==now_dice):
				print('You Win')
			else:
				print('You loss')
				print('The dice is :', end="")
				print(now_dice)
	
	return

# main

game()