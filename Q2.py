'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = len(my_list)           #checking the length of list
for i in range(0,x):       #i gets iterated through the indexes
    if i%2!=0:             #checks if index is odd, then prints the element at odd position
        print(my_list[i])
    
