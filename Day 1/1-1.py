import math
#Calcutes fuel for objects weight defined in 'input'

def main():
    with open('input', 'r') as f:
        line = f.readline()
        fuelNeed = 0
        while line:
            fuelNeed += int(getFuel(line))
            line = f.readline()
        print(fuelNeed)

def getFuel(mass):
    fuel = math.trunc(int(mass) / 3) - 2
    return(fuel)

if __name__ == "__main__":
    main()