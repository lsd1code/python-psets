def main():
    common_words()

def common_words():
    """Visit Project Gutenberg (http://gutenberg.org/ ) and find a few texts you’d like to analyze . Download the text files for these  works, or copy the raw text from your browser into a text file on your computer .
    
    You can use the count() method to find out how many times a word or phrase appears in a string . For example, the following code counts the number of times 'row' appears in a string"""
    
    filename = 'files/trajectory-to-taurus.txt'
    count = 0
    
    try:
        with open(filename) as f_obj:
            contents = f_obj.read().lower().split(' ')
    except FileNotFoundError:
        print(f'{filename} doesn\'t exist')
    else:
        for word in contents:
            word = word.strip()
            
            if word == 'the':
                count += 1
        
        print(f'The word "the" appears {count} times')


def dogs_cats():
    """Make two files, cats.txt and dogs.txt . Store at least three names of cats in the first file and three names of dogs in the second file . Write a program that tries to read these files and print the contents of the file to the screen . Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing . Move one of the files to a different location on your system, and make sure the code in the except block executes properly """
    
    files = ['files/dogs.tx', 'files/cats.txt']
    
    for file in files:
        try:
            with open(file) as f_obj:
                contents = f_obj.readlines()
        except FileNotFoundError:
            # make the program fail silently if file doesn't exist
            pass         
        else:
            for line in contents:
                print(line.rstrip())


def addition():
    """ Write a program that prompts for two numbers . Add them together and print the result . Catch the TypeError if either input value is not a number, and print a friendly error message . Test your program by entering two numbers and then by entering some text instead of a number """
    
    while True:
        x = input('x: ')
        y = input('y: ')
        
        try:
            result = int(x) + int(y)
        except ValueError:
            pass
        else:
            print(f'{x} + {y} = {result}')

if __name__ == "__main__":
    main()