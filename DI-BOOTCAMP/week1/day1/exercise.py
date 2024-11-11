number = input('Give me a number between 1 and 100:')

if int(number) % 5 == 0 and int(number) % 3 == 0:
    print('FizzBuzz')

elif int(number) % 5 == 0:
    print('Buzz')
elif int(number) % 3 == 0:
    print('Fizz')