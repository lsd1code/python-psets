from json import dump, load

def main() -> None:
    favourite_number()


def favourite_number():
    """
    Write a program that prompts for the user’s favorite number . Use json.dump() to store this number in a file . Write a separate program that reads in this value and prints the message, “I know your favorite number! It’s _____ .”
    """
    
    FILENAME = 'files/favourite_number.json'
        
    def store_number() -> None:
        number = input('Enter your favourite number: ')
        
        try:
            number = int(number)
        except ValueError:
            print('Enter a valid integer')
        else:
            with open(FILENAME, 'w') as f:
                dump(number, f)
                print('success...')
    
                
    def get_number() -> None:
        try:
            with open(FILENAME) as f:
                number = load(f)
        except FileNotFoundError:
            print(f'{FILENAME} does not exist')
        else:
            print(f"I know your favorite number! It’s {number}")
                
    store_number()
    
    get_number()

def func():
    """The final listing for remember_me.py assumes either that the user has already entered their username or that the program is running for the first time . We should modify it in case the current user is not the person who last used the program .Before printing a welcome back message in greet_user(), ask the user if this is the correct username . If it's not, call get_new_username() to get the correct username """
    
    pass

if __name__ == '__main__':
    main()