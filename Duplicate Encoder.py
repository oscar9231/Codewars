def duplicate_encode(word):
    new_word = ''
    stack = {}
    i = 0
    while i < len(word):
        if word[i] not in stack:
            stack[word[i].lower()] = 1
            stack[word[i].upper()] = 1
        else:
            stack[word[i].lower()] += 1
            stack[word[i].upper()] += 1
        i += 1
        
    for i in range(0, len(word)):
        if stack[word[i]] == 1:
            new_word += '('
        else:
            new_word += ')'
    return new_word