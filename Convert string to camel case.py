# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.

# Examples:

# # returns "theStealthWarrior"
# to_camel_case("the-stealth-warrior") 

# # returns "TheStealthWarrior"
# to_camel_case("The_Stealth_Warrior")


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
