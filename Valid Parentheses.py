def valid_parentheses(string):
    arr = []
    for c in string:
        if c == '(':
            arr.append(c)
        elif c == ')':
            if arr and arr[-1] == '(':
                arr.pop()
            else:
                return False
    return not arr