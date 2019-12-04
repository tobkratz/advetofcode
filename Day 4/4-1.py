#!/usr/bin/env python3

def bruteforce(a: int, b: int) -> int:
    counter = 0
    while a < b:
        digits = [int(x) for x in str(a)]
        n = len(digits)-1
        i = 0
        adjacent = False
        for i in range(n):
            if(digits[i] == digits[i+1] and adjacent == False):
                j = 0
                incres = 0
                adjacent = True
                for j in range(n):
                    if(digits[0+j] <= digits[1+j]):
                        incres = incres+1
                        if(incres == 5):
                            counter = counter+1
        a = a+1 
    print(counter, "passwords are possible within range")

if __name__ == "__main__":
    bruteforce(387638,919123)