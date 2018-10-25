import random
import time
print("Welcome to Stone,papers and scissors Game")
time.sleep(2)
print("After every 5 turns the winner will be displayed")
time.sleep(3)
time.sleep(4)
z="1"
score_user=0
score_com=0
i=0

while(z!="0"):
	score_user=0
	score_com=0
	i=0
	print(" 1 stone \n 2 paper \n 3 scissors") 
	print("start....")
	while(i<5):
		c=random.choice(["1","2","3"])
		z=input("Your turn ")
		names=["","stone","paper","scissors"]
		print("You have chosen    -----------------    "+names[int(z)])
		time.sleep(2)
		print("Computer has chosen   -----------   "+names[int(c)])
		time.sleep(1)
		if(z=="1" ):
			if(c=="2"):
				score_com+=1
				print("paper folds rock")
			elif(c=="3"):
				score_user+=1
				print("stone breaks scissors")
		elif(z=="2" ):
			if(c=="1"):
				score_user+=1
				print("paper folds rock")
			elif(c=="3"):
				score_com+=1
				print("scissors cuts paper")
		elif(z=="3" ):
			if(c=="2"):
				score_user+=1
				print("scissors cuts paper")
			elif(c=="1"):
				score_com+=1
				print("stone breaks scissors")	
		else:
			print("Wrong input")
			print()
		print("##############################################################################")
		time.sleep(5)
		print("Computer score is   ---------------------------------"+str(score_com))
		print("Your score is  --------------------------------------- "+str(score_user))
		print()
		i+=1
	print()
	time.sleep(2)
	if(score_com>score_user):
		print("Computer is the winner")
	elif(score_com<score_user):
		print("You are the winner")
	elif(score_user==score_com):
		print("Its a draw game")
	time.sleep(1)
	print("If you want to exit press '0'.\n press 'ENTER' to play once again. ")
	z=input()
	print()
	if(z=="0"):
		z="0"
	else:
		z=1
		for i in range(10):
			for j in range(10):
				print()
	
		
