def dig_pow(n, p):
    n_str = str(n)
    i = 0
    sum = 0
    while i < len(n_str):
        sum += int(n_str[i]) ** p
        i += 1
        p += 1
    print(sum/n)
    if (sum/n) == int(sum/n):
        return int(sum/n)
    else:
        return -1