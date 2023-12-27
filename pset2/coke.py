
def main():
    remaining_amount = 50
    
    print(f'Amount due: {remaining_amount}')

    while True:
        coin = int(input('insert coin: '))
        
        remaining_amount -= coin
        
        if remaining_amount > 0:
            print(f'Amount due: {remaining_amount}')
        
        if remaining_amount == 0:
            print(f'Thank You!. Your change is {remaining_amount}')
            break
        elif remaining_amount < 0:
            print(f'Thank You. Your change is {abs(remaining_amount)}')
            break


if __name__ == "__main__":
    main()

"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""