def fizzbuzz(num):
    if (num % 3 == 0) and not (num % 5 == 0):
        return 'Fizz'
    if (num % 5 == 0) and not (num % 3 == 0):
        return 'Buzz'
    if (num % 3 == 0) and (num % 5 == 0):
        return 'FizzBuzz'
    else:
        return num


print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))
print(fizzbuzz(4))
