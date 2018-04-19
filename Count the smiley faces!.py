def count_smileys(arr):
    count = 0
    smileyface = [':D', ':)', ';)', ';D', ':-D', ':-)', ';-D', ';-)', ':~D', ':~)', ';~D', ';~)']
    for face in arr:
        if face in smileyface:
            count += 1
    return count