print('Give me two numbers and I will divide them by two')
print("Enter 'q' to quit")

while True:
    x = input('x: ')
    
    if x.lower() == 'q':
        break
    
    y = input('y: ')
    
    if y.lower() == 'q':
        break
    
    try:
        result = int(x) / int(y)
    except ZeroDivisionError:
        print('You cannot divide by 0')
    else: 
        # any code that depends on the try block being successful
        print(result)