'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n = 5
#Divided the pattern into 2 parts, taking first 5 lines and then next 4 lines
for i in range(0,n):        #i used to iterate through the lines
    for j in range(0,i+1):  #j used to print the stars
        print("*", end="")
    print(" ")
for i in range(0,n-1):
    for j in range(i,n-1):
        print("*", end="")
    print(" ")