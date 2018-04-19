def song_decoder(song):
    song_name = ''
    name_list = song.split('WUB')
    for char in name_list:
        if char != '':
            song_name = song_name + char + ' '
    return song_name[:-1]