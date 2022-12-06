def gcd(num1, num2):
    assert int(num1) == num1 and int(num2) == num2, "the numbers must be integers"
    if num1 < 0:
        num1 *= -1
    if num2 < 0:
        num2 *= -1

    if num2 == 0:
        return num1
    return gcd(num2, num1%num2)



print(gcd(-24, -12))