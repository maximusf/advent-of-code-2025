# Maximus Fernandez
# Advent of Code 2025 - Day 1
# https://adventofcode.com/2025/day/1

from typing import Final

## Circular dial always starts at 50
DIAL_DEFAULT: Final[int] = 50
#DIAL_LOWER_BOUND: Final[int] = 0
DIAL_UPPER_BOUND: Final[int] = 99


"""
Game Plan:

Return the total amount of times the dial is rotated to the '0' position

Need a function that rotates the dial 
in the correct direction and distance
according to the line that is read

After running a rotation, check if the dial's position is currently at 0

If so, zero_count++
else continue reading until end of file

At the end, return zero_count

"""

## Analyze file line by line
def rotateDial(file, dial) -> int:
    zero_count = 0
    for line in file:
        line = line.stip()
        if not line:
            continue

        # checks distance after rotation type
        direction = line[0]
        distance = int(line[1:]) # number after turn direction

        if direction == 'L': # if L --> turn dial towards smaller numbers
            dial = rotateLeft(dial, distance)
        elif direction == 'R': # if R --> turn dial towards larger numbers
            dial = rotateRight(dial, distance)

        # checks if dial is at 0, increment counter
        if dial == 0:
            zero_count += 1
    print("reached end of file")
    return zero_count # returns times dial rotated to '0' position
        

def rotateLeft(dial, distance):
    return (dial - distance) % (DIAL_UPPER_BOUND + 1)

def rotateRight(dial, distance):
    return (dial + distance) % (DIAL_UPPER_BOUND + 1)



def main():
    dial = DIAL_DEFAULT # dial starts at 50
    try:
        with open('input.txt') as file:
            zero_count = rotateDial(file, dial)
        print("The dial rotated to '0' " + str(zero_count) + " times.")
        print("Answer: " + str(zero_count))

    # if input file is not found, error
    except FileNotFoundError:
        print("file does not exist")


if __name__ == "__main__":
    main()