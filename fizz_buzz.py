def fizz_buzz(x):
    if (x%5==0) and (x%3==0):
        return 'FizzBuzz'
    elif x%5==0:
        return 'Buzz'
    elif x%3==0:
        return 'Fizz'
    else:
        return x