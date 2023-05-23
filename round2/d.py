'''
D. Tower

We have 𝑛 towers on a horizontal road. The 𝑖-th tower is located at 𝑎𝑖 and has light intensity 𝑝𝑖 unit.
However, the effect of this tower's light intensity decreases 1 unit for each 1
unit distance away. This means that for position 𝑥,
the light intensity it received from the ith tower will be

max(0,𝑝𝑖−|𝑎𝑖−𝑥|)

For position 𝑗, the light intensity it receives is defined as the maximum light intensity
of the light intensity from all the towers. Given the position of 𝑚 people on the same road,
output the light intensity each of them receives.

-------------------------------------------

INPUT:
The first line contains two integers 𝑛,𝑚 (1≤𝑛,𝑚≤2×105),
representing the number of towers and the number of people.

The next 𝑛 lines each contain two integers 𝑎𝑖,𝑝𝑖 (1≤𝑎𝑖,𝑝𝑖≤109),
representing the position and intensity of the 𝑖-th tower.

The last line contains 𝑚 integers 𝑏1,𝑏2,…,𝑏𝑚 (1≤𝑏𝑖≤109),
representing the position of each person.

OUTPUT:
On the 𝑖-th line, output the light intensity received by the 𝑖-th person.
'''

def main():
    ntowers = int(str(input()).split(" ")[0])

    towers = []

    for i in range(ntowers + 1):
        towers.append([int(x) for x in str(input()).split(" ")])

    get_light(towers.pop(), towers)

def get_light(people, towers):
    for x in people:
        lrs = [light_received(x, i, towers) for i in range(len(towers))]
        lrs.sort() #attempt to make it run in less time ;-;
        print(int(lrs.pop()))
        
def light_received(x, i, towers):
    return max(0, towers[i][1] - abs(towers[i][0] - x))

main() #DOES NOT RUN IN 1000MS