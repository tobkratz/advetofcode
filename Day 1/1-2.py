import math
#Calcutes fuel for fuel for objects weight defined in 'input'

def main():
    with open('input', 'r') as f:
        line = f.readline()
        totalFuel = 0
        while line:
            totalFuel += getFuelFuel(line)
            line = f.readline()
        print(totalFuel)

def getFuel(mass):
    fuel = int(int(mass) / 3) - 2
    return(fuel)

def getFuelFuel(mass):
    fuelMass = getFuel(int(mass))
    lastFuel = fuelMass
    while lastFuel > 0:
        lastFuel = getFuel(lastFuel)
        if lastFuel > 0:
            fuelMass += lastFuel
    return(fuelMass)

if __name__ == "__main__":
    main()