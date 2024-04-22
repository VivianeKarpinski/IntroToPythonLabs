"""
INSTRUCTIONS:
Create a Python solution to the following task. Ensure that the solution produces output exactly the same format
shown in the sample(s) below, including capitalization and whitespace.

TASK:
Create a solution that accepts an input identifying the name of a text file, for example, "WordTextFile1.txt".
Each text file contains three rows with one word per row. Using the open() and write(), and read() methods, interact
with the input text file to write a new sentence string composed of the three existing words to the end of the file
contents on a new line. Output the new file contents

The solution should be in the format
word1
word2
word3
sentence

If the input is 
WordTextFile1.txt

Then the expected is
cat
chases
dog
cat chases dog

"""

#open, write, and read text file (e.g., "WordTextFile1.txt") using open(), write(), read()
#solution accepts file input to insert sentence composed of file content into text file on a new line
#solution outputs the text file contents including the new sentence

file = input()

with open(file, 'r+') as x:
    conts= x.readlines() 
    for a in conts:
        print(a.strip())

with open(file, 'r+') as f:
    lines = []
    for i in f:
        i = i.strip()        
        lines.append(i)       
print(' '.join(lines))
