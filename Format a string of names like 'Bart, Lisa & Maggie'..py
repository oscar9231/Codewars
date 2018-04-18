def namelist(names):
    b = ""
    i = 0
    if len(names) == 0:
        return ''
    elif len(names) < 2:
        return names[0]['name']
    elif len(names) == 2:
        return names[0]['name'] + ' ' + '&' + ' ' + names[1]['name']
    elif len(names) > 2:
        while i < (len(names) - 1):
            b = b + names[i]['name'] + ',' + ' '
            i += 1
        return b[:-2] + ' ' + '&' + ' ' + names[len(names)-1]['name']