'''
A. Bad Grades

Michael received some very bad grades in his classes at Andover. He has taken 𝑛 classes.
Each class gives Michael a grade in the range from 0 to 100. Michael doesn't want to fail any classes,
so he hacked into the school's computer system to remove all class grades <60 from his transcript. 
Given a list of 𝑛 numbers, each number is in the range from 0 to 100, remove all elements <60
from Michael's list of grades.

-------------------------------------------

INPUT:
The first line contains a number 𝑛 (1≤𝑛≤105) The next 𝑛 lines each contains one of Michael's grades.
Each grade is in the range [0,100].

OUTPUT:
Output the new list of grades. You should not change the ordering of Michael's grades.
'''
def main():
    lines = int(input())
    grades = []
    for i in range(lines):
        grades.append(int(input()))
    
    for i in grades:
        if i >= 60:
            print(i)

main() #CORRECT

    