"""
33.14 LAB: Palindrome

A palindrome is a word or a phrase that is the same when read both forward and backward. 
Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). 
Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

Ex: If the input is:

bob
the output is:

bob is a palindrome
Ex: If the input is:

bobby
the output is:

bobby is not a palindrome
Hint: Start by removing spaces. Then check if a string is equivalent to it's reverse.

"""
def is_palindrome(word_check):
    w_no_space = word_check.replace(' ', '')
    if w_no_space[::-1] == w_no_space:
        print(f'{word_check} is a palindrome')
    else:
        print(f'{word_check} is not a palindrome')

if __name__ == '__main__':
    word_inp = str(input())
    is_palindrome(word_inp)

