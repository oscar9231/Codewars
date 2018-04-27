def validBraces(string):
    pairs = {'(' : ')', '[' : ']', '{' : '}'}
    brace_left = pairs.keys()
    brace_right = pairs.values()
    valid_pairs = []
    for n in string:
        if n in brace_left:
            valid_pairs.append(n)
        elif valid_pairs and n in brace_right and pairs[valid_pairs[-1]] == n:
            valid_pairs.pop()
    if valid_pairs:
        return False
    else:
        return True