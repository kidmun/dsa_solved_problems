def powerOfNumber(base, exp):
    assert exp >= 0 and int(exp) == exp, "the exponent has to be integer and greater than zero"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * powerOfNumber(base, exp - 1) 

