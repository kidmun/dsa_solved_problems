def sumOfDigits(number):
    assert number >= 0 and int(number), "the number has tobe positive integer"
    if number == 0:
        return 0
    return number % 10 + sumOfDigits(int(number/10))

