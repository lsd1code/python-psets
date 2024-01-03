# json module
import json 

def main():
   load_json() 

def load_json():
    filename = 'files/numbers.json'
    try:
        with open(filename) as f_obj:
            numbers = json.load(f_obj)
    except FileNotFoundError:
        print(f'{filename} does not exist')
    else:
        print(numbers)
    
# saving python data in a json file
def save_json() -> None:
    numbers = [(i + 1) for i in range(100)]
    filename = 'files/numbers.json'

    with open(filename, 'w') as f_obj:
        json.dump(numbers, f_obj)
        print('completed successfully')

if __name__ == '__main__':
    main()