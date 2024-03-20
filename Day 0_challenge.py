###To complete this challenge, you must save a line of input from stdin to a variable, print Hello, World. on a single line, and finally print the value of your variable on a second line.
You've got this!
Input format:
A single line of text denoting inputstring  (the variable whose contents must be printed).
Output format:
Print Hello, World. on the first line, and the contents input string of  on the second line.
Sampple input:
Welcome to 30 Days of Code!
Sample output:
Hello, World. 
Welcome to 30 Days of Code!
  ###
code:
# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = input()

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')

# TODO: Write a line of code here that prints the contents of input_string to stdout.
print(input_string)
