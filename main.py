from math import sqrt
number=int(input('Enter your number-'))
print('\n')
if number>1:
    for i in range(2,int(sqrt(number))+1):
        if(number%i)==0:
            print(number,'Is not a prime number')
            break
    else:
        print(number,'Is a prime number')
