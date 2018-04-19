def pig_it(text):
    words = text.split()
    text_new = ''
    for word in words:
        word = word[1:] + word[0]
        text_new = text_new + word + 'ay '
    if words[-1] in ['!', '?']:
        return text_new[:-3]
    else:
        return text_new[:-1]