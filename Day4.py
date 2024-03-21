'''
Task
Write a Person class with an instance variable,age , and a constructor that takes an integer,initial age , as a parameter. 
The constructor must assign initial age  to age  after confirming the argument passed as initialage is not negative; 
if a negative argument is passed as age , the constructor should set age  to 0  and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:

yearPasses() should increase the  instance variable by .
amIOld() should perform the following conditional actions:
If , print You are young..
If  and , print You are a teenager..
Otherwise, print You are old..
To help you learn by example and complete this challenge, much of the code is provided for you, but you'll be writing everything in the future. The code that creates each instance of your Person class is in the main method. Don't worry if you don't understand it all quite yet!

Note: Do not remove or alter the stub code in the editor.
Input Format

Input is handled for you by the stub code in the editor.

The first line contains an integer, T (the number of test cases), and the T subsequent lines each contain an integer denoting the age of a Person instance.
Constraints
1<=T<=4
5<=T<=20
Output Format
Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test your work is already in the editor.
If your methods are implemented correctly, each test case will print 2 or 3 lines (depending on whether or not a valid initial age was passed to the constructor).

Sample Input

4
-1
10
16
18
Sample Output

Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.
'''
code:
class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge=initialAge
        if (self.initialAge<0):
            self.initialAge=0
            print("Age is not valid, setting age to 0.")
            
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if (self.initialAge<13):
            print("You are young.")
        elif (self.initialAge>=13 and self.initialAge<18):
            print("You are a teenager.")
        else:
            print("You are old.")
            
    def yearPasses(self):
        # Increment the age of the person in here
        self.initialAge = self.initialAge+ 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
