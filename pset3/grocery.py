def main():
    items = {}
    
    while True:
        try:
            item = input('Item: ').upper()       
        except KeyboardInterrupt:
            print()
            break
        
        if not item:
            continue
        
        if not items.get(item):
            items[item] = 1 # add item to the dict and set initial value to one
        else:
            items[item] = items[item] + 1
            
    for item in sorted(items):
        print(f'{items[item]} {item}')


if __name__ == '__main__':
    main()
    

"""
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.
"""