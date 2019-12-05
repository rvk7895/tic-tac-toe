import time
from os import system, name

system('clear')

elements=[['-','-','-'],['-','-','-'],['-','-','-']] #elements in the grid
player=-1 #which player chance is right now 1 represent x 2 represent o
x=-1	#x co-ordinate at which the player is putting his/her dot or cross
y=-1 #y co-ordinate at which the player is putting his/her dot or cross
score1=0
score2=0


def grid():
	system('clear')
	print("\t\t\t\t\t\t\t\t\t\t\t       1   2   3")
	for r in range(0,9):
		if(r==1 or r==4 or r==7):
			if(r==1):
				print("\t\t\t\t\t\t\t\t\t\t\t    1 ",elements[0][0],"|",elements[0][1],"|",elements[0][2]) #prints the elements in the grid
			if(r==4):
				print("\t\t\t\t\t\t\t\t\t\t\t    2 ",elements[1][0],"|",elements[1][1],"|",elements[1][2]) #prints the elements in the grid
			if(r==7):
				print("\t\t\t\t\t\t\t\t\t\t\t    3 ",elements[2][0],"|",elements[2][1],"|",elements[2][2]) #prints the elements in the grid
			continue
		print("\t\t\t\t\t\t\t\t\t\t\t         |   |   ")
		if((r+1)%3==0 and r!=8):
			print("\t\t\t\t\t\t\t\t\t\t\t      -----------")#prints the hyphen

#checks if the player has won
def win(char):
	count=0
	i=0
	while i<3:
		j=0
		while j<3:
			if(char==elements[i][j] and elements[i][j]!='-'):
				count+=1
			j+=1
		if(count==3):
			return  True
			break
		count=0
		i+=1
	count=0	
	i=0
	while i<3:
		j=0
		while j<3:
			if(char==elements[j][i] and elements[j][i]!='-'):
				count+=1
			j+=1
		if(count==3):
			return  True
			break
		count=0
		i+=1
	count=0
	i=0
	while i<3 :
		if(char==elements[i][i] and elements[i][i]!='-'):
				count+=1
		if(count==3):
			return  True
			break
		i+=1
	count=0		
	i=0	
	while i<3 :
		if(char==elements[i][2-i] and elements[i][2-i]!='-'):
				count+=1
		if(count==3):
			return  True
			break
		i+=1
	count=0

#check if its a draw
def draw(): 
	count=0
	for i in range(0,3):
		for j in range(0,3):
			if(elements[i][j]!='-'):
				count+=1
	if (count == 9):
		return True


print("\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tTHE GAME OF TIC TAC TOE")
time.sleep(1)
print("\t\t\t\tPlayer 1 is x and Player 2 is o")
time.sleep(1)
player1=input("\t\t\t\tPlayer 1 enter your name ")
player2=input("\t\t\t\tPlayer 2 enter your name ")
print("\t\t\t\tPlayer 1 goes first")
time.sleep(1)

#main
winflag=False
drawflag=False
player=1
invalid=False

while True:
	grid()
	if(player==1):
		print("Its",player1,"\b's turn")
	if(player==2):
		print("Its",player2,"\b's turn")
	if(invalid):
		print("\n\t\tInvalid input!!\n\t\tA player has already played his move in that position. Try again.")
		invalid=False
	x,y=input("\nInput the x and y co-ordinate where you want to place your symbol respectively: ").split()
	x=int (x,10)
	y=int (y,10)
	if(elements[y-1][x-1]!='-'):
		invalid=True
		continue
	
	#where the element element is inserted in the grid
	if(player==1):
		elements[y-1][x-1]='x'
		player=2
		grid()
	elif(player==2):
		elements[y-1][x-1]='o'
		player=1
		grid()
	
	#where checking takes place
	if(player == 2):
		winflag=win("x")
		if(winflag):
			print("\t\t\t\t\t\t\t\t\t\t\t",player1,"won!!")
			score1+=1

	elif(player == 1):
		winflag=win("o")
		if(winflag):
			print("\t\t\t\t\t\t\t\t\t\t\t",player2,"won!!")
			score2+=1
			
	drawflag=draw()
	if(drawflag and not(winflag)):
		print("\t\t\t\t\t\t\t\t\t\t\tIts a Draw!!")
	if(winflag or drawflag):
		print("\n\t\t\t\t\t\t\t\t\t\t\t",player1,"\b:",score1,"\n\t\t\t\t\t\t\t\t\t\t\t",player2,"\b:",score2)
		game=input("\t\t\t\t\t\t\t\t\t\tWanna play another game??(y or n)")

		if(game=='y'):
			for i in range(0,3):
				for j in range(0,3):
					elements[i][j]='-'
			winflag=False
			drawflag=False
			player=1

		else:
			if(score1>score2):
				print("\t\t\t\t\t\t\t\t\t\t",player1,"won the game!!")
			elif(score2>score1):
				print("\t\t\t\t\t\t\t\t\t\t",player2,"won the game!!")
			else:
				print("\t\t\t\t\t\t\t\t\t\tIt's a Draw!!")
			break