'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
x = "The quick Brow Fox"
ucount =0                 #created counter for upper elements
lcount = 0                #created counter for lower elements
for i in x:               # i gets iterated through the given string
    if i.isupper():       #checking the upper case elements and incrementing the count value
        ucount = ucount+1 
    elif i.islower():     #checking the lower case elements and incrementing the count value
        lcount = lcount+1
print("No. of Upper-case characters:",ucount)
print("No. of Upper-case characters:",lcount)

