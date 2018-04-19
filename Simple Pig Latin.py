# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# Examples

# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldWay !


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
