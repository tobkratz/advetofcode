import array as array
#Intcode Reader with 1 as + and 2 as * with search for verb and noun for a specified output

def main():
    for i in range(100):
        for j in range(100):
            a = readFile()
            a[1] = i # noun
            a[2] = j # verb
            a = optcode(a)
            if int(a[0]) == 19690720:
                print 'Incode program finished with value at 0: ', a[0], ' with noun: ', a[1], 'and verb: ', a[2]
                break
            else:
                #a.clear
                continue

def readFile():
    with open('input', 'r') as f:
        a = []
        for line in f:
            a = line.split(",")
    return(a)

def optcode(a):
    i = 0
    while i < len(a):
        if int(a[i]) == 1:
            a[int(a[i+3])] = int(a[int(a[i+1])]) + int(a[int(a[i+2])])
            i = i+4
            continue 
        if int(a[i]) == 2:
            a[int(a[i+3])] = int(a[int(a[i+1])]) * int(a[int(a[i+2])])
            i = i+4
            continue
        if int(a[i]) == 99:
            return(a)
    
if __name__ == "__main__":
    main()