import sys, os, tty, termios

f = open(sys.argv[1], 'r')

cell = [0]   #cells
ptr = 0      #data pointer
llp = []     #last loop position
fpos = 0     #file position

fsize = os.path.getsize(sys.argv[1])

while fpos < fsize:
	f.seek(fpos)
	cin = f.read(1)

	if(cin == '+'):
		cell[ptr] += 1

	elif(cin == '-'):
		cell[ptr] -= 1

	elif(cin == '>'):
		if((len(cell) - 1) == ptr): #pointer is on last cell
			cell.append(0) #add new cell to the end
		ptr += 1

	elif(cin == '<'):
		if(ptr == 0):
			print("ERRRRROOOOOORRRRRRR")
		else:
			ptr -= 1
	
	elif(cin == '['):
		llp.append(fpos)

	elif(cin == ']'):
		if(cell[ptr] != 0):
			fpos = llp[-1]
		else:
			llp.pop()

	elif(cin == '.'):
		print(chr(cell[ptr]), end='')

	elif(cin == ','):
		cell[ptr] = ord(input())

	fpos += 1
