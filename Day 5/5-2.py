import array as array

class COMPUTER:
	def readFile():
		with open('input', 'r') as f:
			a = []
			for line in f:
				a = line.split(",")
		return(a)


	def execute(a):
		i = 0
		inOut = [5] # In/Output Buffer. start with 1 as System Unit (given)
		while i < len(a):
			iString = str(a[i])
			if int(iString[len(iString)-1]) == 1: #instruction 1 menas add
				a = OP.ADD(a,i)
				i = i+4
				continue 
				
			if int(iString[len(iString)-1]) == 2: #instruction 2 menas Mul
				a = OP.MUL(a,i)
				i = i+4
				continue

			if int(iString[len(iString)-1]) == 3: #instruction 3 menas Store
				a = OP.STR(a,i,inOut[len(inOut)-1])
				i = i+2
				continue

			if int(iString[len(iString)-1]) == 4: #instruction 4 menas Print to In/Output Buffer
				inOut.append(OP.PRINT(a,i))
				i = i+2
				continue
			
			if int(iString[len(iString)-1]) == 5: #instruction 5 menas jump if true
				i = OP.JUMP_IF_TRUE(a,i)
				continue
			
			if int(iString[len(iString)-1]) == 6: #instruction 6 menas jump if false
				i = OP.JUMP_IF_FALSE(a,i)
				continue

			if int(iString[len(iString)-1]) == 7: #instruction 6 menas less than
				a = OP.LESS_THAN(a,i)
				i = i+4
				continue

			if int(iString[len(iString)-1]) == 8: #instruction 8 means equal
				a = OP.EQUALS(a,i)
				i = i+4
				continue

			if int(iString[len(iString)-1]) == 9 & int(iString[len(iString)-2]) == 9:  #Instruction 99 menas halt
				return(inOut)
			
class OP:
	def ADD(a,i): #adds the 2 Numbers after the Instruction together and store them at pos. given in i+3
		iString = "0000" + str(a[i]) # adds 4 "0" to the beginning of the instruction, to fill if instruction is in position mode
		
		if int(iString[len(iString)-3]) == 1: 
			first = int(a[i+1]) #immediate mode
		else:
			first = int(a[int(a[i+1])]) #Position Mode

		if int(iString[len(iString)-4]) == 1:
			second = int(a[i+2]) #immediate mode
		else:
			second = int(a[int(a[i+2])]) #Position Mode

		a[int(a[i+3])] = first + second
		return(a)

	def MUL(a,i): #multiplies the 2 Numbers after the Instruction together and store them at pos. given in i+3
		iString = "0000" + str(a[i])
		
		if int(iString[len(iString)-3]) == 1:
			first = int(a[i+1]) #immediate mode
		else:
			first = int(a[int(a[i+1])]) # position mode

		if int(iString[len(iString)-4]) == 1:
			second = int(a[i+2]) # immediate mode
		else:
			second = int(a[int(a[i+2])]) # position mode

		a[int(a[i+3])] = first * second
		return(a)

	def STR(a,i,inOut):
		a[int(a[i+1])] = inOut # stores the last Output from Buffer in Array Position
		return(a)

	def PRINT(a,i):
		iString = "0000" + str(a[i])
		if int(iString[len(iString)-3]) == 1:
			return(int(a[i+1]))
		else:
			return(int(a[int(a[i+1])]))
	
	def JUMP_IF_TRUE(a,i):
		iString = "0000" + str(a[i])
		if int(iString[len(iString)-3]) == 1: #immediate mode of first parameter
			if int(a[i+1]) != 0: 
				if int(iString[len(iString)-4]) == 1: #immediate mode of second parameter
					return(int(a[i+2]))
				else: #position mode of second parameter
					return(int(a[int(a[i+2])]))
			else:
				return(i+3)
		else: # Position mode of first parameter
			if int(a[int(a[i+1])]) != 0:
				if int(iString[len(iString)-4]) == 1: #immediate mode of second parameter
					return(int(a[i+2]))
				else: #position mode of second parameter
					return(int(a[int(a[i+2])]))
			else:
				return(i+3)

	def JUMP_IF_FALSE(a,i):
		iString = "0000" + str(a[i])
		if int(iString[len(iString)-3]) == 1: #immediate mode of first parameter
			if int(a[i+1]) == 0:
				if int(iString[len(iString)-4]) == 1: #immediate mode of second parameter
					return(int(a[i+2]))
				else: #position mode of second parameter
					return(int(a[int(a[i+2])]))
			else:
				return(i+3)
		else: # Position mode of first parameter
			if int(a[int(a[i+1])]) == 0:
				if int(iString[len(iString)-4]) == 1: #immediate mode of second parameter
					return(int(a[i+2]))
				else: #position mode of second parameter
					return(int(a[int(a[i+2])]))
			else:
				return(i+3)

	def LESS_THAN(a,i):
		iString = "0000" + str(a[i])
		if int(iString[len(iString)-3]) == 1:
			first = int(a[i+1]) #immediate mode
		else:
			first = int(a[int(a[i+1])]) # position mode

		if int(iString[len(iString)-4]) == 1:
			second = int(a[i+2]) # immediate mode
		else:
			second = int(a[int(a[i+2])]) # position mode

		if first < second:
			a[int(a[i+3])] = 1
		else:
			a[int(a[i+3])] = 0
		return(a)


	def EQUALS(a,i):
		iString = "0000" + str(a[i])
		if int(iString[len(iString)-3]) == 1:
			first = int(a[i+1]) #immediate mode
		else:
			first = int(a[int(a[i+1])]) # position mode

		if int(iString[len(iString)-4]) == 1:
			second = int(a[i+2]) # immediate mode
		else:
			second = int(a[int(a[i+2])]) # position mode

		if first == second:
			a[int(a[i+3])] = 1
		else:
			a[int(a[i+3])] = 0
		return(a)

def main():
    a = COMPUTER.readFile()
    print('Incode programm finished with last output: ', COMPUTER.execute(a))
	
if __name__ == "__main__":
	main()