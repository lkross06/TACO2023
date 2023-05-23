'''
B. glimmerypond

Daniel is given a 2D grid representing an 𝑛×𝑚 pond, 
where each cell can either be filled with water or be empty. The grid is considered glimmery 
if the number of water-filled cells in any square subgrid of size 𝑘×𝑘 is divisible by 2.

Help Daniel write a function that determines whether a given pond is glimmery or not.

-------------------------------------------

INPUT:
The input parameters are:

𝑛,𝑚,𝑘 each separated by a single space. 𝑛 is the number of rows in the pond.
𝑚 is the number of columns in the pond. Both 𝑛,𝑚 satisfy 1≤𝑛,𝑚≤100.
𝑘 satisfies 1≤𝑘≤min(𝑛,𝑚).

This is followed by 𝑛 lines. Each line contains 𝑚 integers, 
where 0 denotes an empty cell and 1 represents a water-filled cell.

OUTPUT:
Ouput "true" if the pond is glimmery, "false" if not.
'''
def main():
    inputs = [int(x) for x in str(input()).split(" ")]
    row = inputs[0]
    col = inputs[1]
    k = inputs[2]

    pond = []
    for i in range(row):
        pond.append([int(x) for x in str(input()).split(" ")])

    print(search(pond, k))

def search(pond, k):
    for i in range(len(pond) - (k - 1)):
        for j in range(len(pond[0]) - (k - 1)):
            #look at each item in grid
            if apply_grid(pond, i, j, k):
                return "true"
    return "false"

def apply_grid(pond, i, j, k):
    water = 0
    for k in range(i, i + k):
        for l in range(j, j + k):
            if pond[i][j] == 1:
                water += 1
    if water % 2 == 0:
        return True
    return False

main() #CORRECT