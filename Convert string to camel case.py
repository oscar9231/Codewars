def to_camel_case(text):
    if text == '':
        return ''
    character_list = []
    new_string = ''
    for n in text:
        character_list.append(n)
    i = 0
    while i < len(character_list):
        if character_list[i] in ['-', '_']:
            character_list[i+1] = character_list[i+1].upper()
        i += 1
    for n in character_list:
        if n not in ['-', '_']:
            new_string += n
    return new_string