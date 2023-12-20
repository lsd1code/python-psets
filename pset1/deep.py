def main():
    answer = input('What is the answer to the Great question of Life, the Universe and Everything?: ').strip()
    
    if (
            answer.lower() == 'forty-two' 
            or answer.lower() == 'forty two' 
            or int(answer) == 42
        ):
        print('Yes')
    else:
        print('No')


main()

"""
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
"""