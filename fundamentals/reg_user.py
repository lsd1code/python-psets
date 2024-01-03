import json

def main():
    greet_user()


def greet_user():
    name = input('Name: ')

    filename = 'files/users.json'
    
    with open(filename) as f:
        name_json = json.load(f)
        
        if name == name_json.lower():
            print(f'Welcome back, {name_json.title()}')
        else:
            print('You are not a registered user')


def register_user():
    name = input('Name: ')

    filename = 'files/users.json'

    with open(filename, 'a') as f_obj:
        json.dump(name, f_obj)
        print(f'We will remember you when you come back {name.title()}')
    
if __name__ == "__main__":
    main()