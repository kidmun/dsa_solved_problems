def decimalToBinary(number):
    assert int(number) == number and number >= 0, "the number has to be positive and integer"
    if number == 0:
        return 0
    return number % 2 + 10 * decimalToBinary(int(number/2))



print(decimalToBinary(10))
print(decimalToBinary(-1))
print(decimalToBinary(34))
print(decimalToBinary(256))