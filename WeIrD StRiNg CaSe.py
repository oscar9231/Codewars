def to_weird_case(string):
    words = string.split(' ')
    j = 0
    weird_word = ''
    while j < len(words):
        odd = ''
        even = ''
        weird = ''
        i = 0
        while i < len(words[j]):
            if i == 0 or i % 2 == 0:          #even bit
                even += words[j][i]
            else:
                odd += words[j][i]
            i += 1
        even = even.upper()
        if len(even) == len(odd):
            n = 0
            while n < len(odd):
                weird += even[n] + odd[n]
                n += 1
        elif len(even) > len(odd):
            n = 0
            while n < len(odd):
                weird += even[n] + odd[n]
                n += 1
            weird += even[-1]
        else:
            n = 0
            while n < len(even):
                weird += even[n] + odd[n]
                n += 1
            weird += odd[-1]
        weird_word += weird + ' '
        j += 1
    return weird_word[:-1]