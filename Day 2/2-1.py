import array as array
#Intcode Reader with 1 as + and 2 as * with search for verb and noun for a specified output

def main():
    a = readFile()
    a[1] = 12 # noun
    a[2] = 2 # verb
    a = optcode(a)
    print('Incode programm finished with value at 0: ', a[0], ' with noun: ', a[1], 'and verb: ', a[2])

def readFile():
    with open('input', 'r') as f:
        a = []
        for line in f:
            a = line.split(",")
    return(a)

def optcode(a):
    i = 0
    while i < len(a):
        if int(a[i]) == 1: #Optcode 1 adds the 2 Numbers after the Instruction together and store them at pos. given in i+3
            a = optcodeAdd(a,i)
            i = i+4
            continue 
        if int(a[i]) == 2: #Optcode 2 does same as 1 except multiplies instead of adds 
            a = optcodeMul(a,i)
            i = i+4
            continue
        if int(a[i]) == 99:
            return(a)
    
def optcodeAdd(a,i):
    a[int(a[i+3])] = int(a[int(a[i+1])]) + int(a[int(a[i+2])])
    return(a)

def optcodeMul(a,i):
    a[int(a[i+3])] = int(a[int(a[i+1])]) * int(a[int(a[i+2])])
    return(a)

if __name__ == "__main__":
    main()