def main():
    file = input('Filename: ').strip().lower()
    
    if not '.' in file:
        print('application/octet-stream')
    else:
        _, extension = file.split('.')
        
        match extension:
            case 'gif':
                print('image/gif')
            case 'jpg' | 'jpeg':
                print('image/jpeg')
            case 'png':
                print('image/png')
            case 'pdf':
                print('application/pdf')
            case 'txt':
                print('text/plain')
            case 'zip':
                print('appliation/zip')
            case _:
                print('application/octet-stream')


main()


"""
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif -> image/gif
.jpg -> image/jpeg
.jpeg -> image/jpeg
.png -> image/png
.pdf -> application/pdf
.txt -> text/palin
.zip -> application/zip

If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""