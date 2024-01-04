import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        print('Two few command-line arguments')
        sys.exit()
    if len(sys.argv) > 2:
        print('Two many command-line arguments')
        sys.exit()
        
    _, read_file = sys.argv
    
    if read_file[-4:].lower() != '.csv':
        print('Not a csv file')
        sys.exit()  
            
    try:
        with open(read_file) as f:
            reader = csv.reader(f)

            menu = [line for line in reader]
    except FileNotFoundError:
        print('File not found')
        sys.exit()
    else:
        print(tabulate(menu, headers='firstrow', tablefmt='outline'))
        


if __name__ == '__main__':
    main()