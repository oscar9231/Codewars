def countBits(n):
    a = bin(n)[2:]
    return a.count('1')