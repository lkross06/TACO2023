'''
A. 01 (Easy Version)

You have a binary string 𝑆, which is a string only containing 0s and 1s. 
You can perform the following operation to 𝑆 any number of times:

Choose a substring 01 and delete it from the string.

Output the string left when it's impossible to do any more operations.

-------------------------------------------

INPUT:
A single line with a binary string 𝑆

OUTPUT:
Output two lines, the length of the final string and the final string.
'''

def operation(s): #performs the operation
    return str(s).replace("01", "", 1)

def main():
    string = input()
    while True:
        sold = string
        string = operation(string) #keep performing operation
        if sold == string: #if the operation doesnt change the string (i.e. no more "01" left)
            #print the deliverables
            print(len(string))
            print(string)
            break

main() #CORRECT
