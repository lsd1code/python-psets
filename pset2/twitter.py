def main():
    string = input('Input: ')
    
    # classic for-loop (solution 1)
    # output = ''
    # for char in string:
    #     if char in ['a', 'e', 'i', 'o', 'u']:
    #         continue
    #     output += char
    
    # list comprehension (solution 2)
    output = ''.join([char for char in string if char not in 'aeiou'])

    print(f'Output: {output}')

if __name__ == "__main__":
    main()

"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

Exapmles:
  `Twitter` -> `Twttr`
  `What's your name?` -> `Wht's yr nm?`
"""