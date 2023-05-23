'''
C. No 7

Gunga doesn't like the number 7. Given a positive integer 𝑥,
try to find the maximum integer smaller than 𝑥 that does not contain a 7 on any of its digits.

-------------------------------------------

INPUT:
A single integer 𝑥 (1≤𝑥≤104).

OUTPUT:
The maximum integer smaller than 𝑥 that does not contain a 7 on any of its digits.
'''
def main():
    num = int(input()) - 1
    
    while True:
        s = [int(x) for x in str(num)]
        if not(7 in s):
            print(num)
            break
        num -= 1

main() #CORRECT