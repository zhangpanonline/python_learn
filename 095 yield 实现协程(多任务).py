def sing():
    for i in range(5):
        print('sing...')
        yield 
        
        
def song():
    for i in range(5):
        print('song....')
        yield 
        

if __name__ == '__main__':
    my_sing = sing()
    my_song = song()
    is_sing = None
    is_song = None
    
    while True:
        try:
            next(my_sing)
        except StopIteration:
            is_sing = True
        try:
            next(my_song)
        except StopIteration:
            is_song = True
        if is_song and is_sing:
            break
        
    