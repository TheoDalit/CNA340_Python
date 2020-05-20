number = int(input('Pick a number between 1 to 100:\n'))
#Prints "Fizz" multiples of 3, "Buzz" multiples of 5, "FizzBuzz" multiples of 3 & 5, number everything else

if number >= 1 and number <= 100:
    if number % 3 == 0:
        if number % 5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif number % 5 == 0:
        if (number % 3 ==0):
            print('FizzBuzz')
        else:
            print('Buzz')
    else:
        print(number)
else:
    print(number)


