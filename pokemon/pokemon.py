import random

def map():
	li = []
	
	x = 0
	y = 0
	
	file = open("map.txt", "r")
	raw = file.read().split("\n")
	
	for row in range(len(raw)):
		f = raw[row].split(",")
		li.append([])
	
		for col in range(len(f)):
			if f[col] == "0":
				print("o", end = " ")
				li[row].append("o")
	
			if f[col] == "1":
				print("x",end = " ")
				li[row].append("o")
				x = col
				y = row 
	
			if f[col] == "2":
				print("#", end = " ")
				li[row].append("#")
	
		print(" ")
	
	for i in range (0,8):
		if raw[i] == "0":
			li[y][x] = "o"
	
		elif raw[i] == "2":
			li[y][x] = "#"
	file.close()



def random_prob():
	prob = random.randint(0, 5)
	if prob == 0:
		print("A wild pokemon has appeard!")
		
map()

print("==============")
print("     MENU     ")
print("==============")
print("1. move up")
print("2. move down")
print("3. move left")  
print("4. move right")
print("5. save and exit game")



while 1:  	

	choice = int(input("choose action: "))
	if choice == "1":
		print("move up")
		if ( y - 1 >= 0):
			y -= 1

	if choice == "2":
		print("move down") 
		if ( y + 1 <= 7):
			y += 1

	if choice == "3":
		print("move left")
		if ( x - 1 >= 0):
			x -= 1

	if choice == "4":
		print("move right")
		if ( x + 1 <= 7):
			x += 1

	if choice == "5":
		print("game saved")
		break

	else:
		("invalid input")