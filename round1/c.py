'''
C. Number Machine

Harry has a strange number machine that has two buttons.
The machine has a number 𝑥 on its screen.
- If button A is pressed, the number on the screen changes to 3𝑥+2. 
- If button B is pressed, the number on the screen changes to 𝑥+1. 

The initial number on the machine is 1, and Harry wants to change the number to 𝑛. 
Harry is lazy so he wants to press the least number of buttons possible.

What is the minimum number of button presses Harry has to make in order to obtain the number 𝑛?

-------------------------------------------

INPUT:
The first line contains the integer 𝑛 (1 ≤ 𝑛 ≤ 10^18).

OUTPUT:
Output a single integer denoting the minimum number of button presses.
'''

def an(n): #reverts a button A press
    #a(x) = 3x + 2 ----> a'(n) = (n - 2)/3
    return (n - 2) / 3

def bn(n): #reverts a button B press
    #b(x) = x + 1 ----> b'(n) = n - 1
    return n - 1

def change(n, i): #work backwards from n --> 1 by performing the inverse of each button
    if n == 1: #BASE CASE
        return i
    if n == 0: #JUST IN CASE
        return i - 1
    if n < 5: #if it reaches 4 then we have to go 4 --> 3 --> 2 --> 1
        return i + (n - 1)

    if n % 3 == 2: #case 1: 2 remainder, we can just revert a button A press
        return change(an(n), i + 1)
    elif n % 3 == 0: # case 2: no remainder, we revert button B press then its case 1
        return change(an(bn(n)), i + 2)
    else: #case 3: 1 remainder, we revert button B press then its case 2
        return change(an(bn(bn(n))), i + 3)

def main():
    print(int(change(int(input()), 0)))

main() #FAILED ON TEST CASE 3