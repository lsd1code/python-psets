# Handling file not found exceptions: <FileNotFoundError>
def main():
    files = ['alice.txt', 'lord-of-the-rings.txt', 'willy-wonka.txt', 'moby-dick.txt', 'wonka.txt']
    
    for file in files:
        filepath = f'files/{file}'
        word_count(filepath)


def word_count(filename='alice.txt'):
    try:
        with open(filename, 'r') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print(f'{filename} does not exist!')
    else:
        words = contents.split(' ')
        print(f'The file has {len(words)} words.')
        

if __name__ == '__main__':
    main()