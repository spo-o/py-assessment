import sys

def rush(x, y):

    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):

        line = ""

        for col in range(x):

            # corners
            if (
                (row == 0 and col == 0) or
                (row == 0 and col == x - 1) or
                (row == y - 1 and col == 0) or
                (row == y - 1 and col == x - 1)
            ):
                line += "o"

            # top and bottom borders
            elif row == 0 or row == y - 1:
                line += "-"

            # left and right borders
            elif col == 0 or col == x - 1:
                line += "|"

            # inside spaces
            else:
                line += " "

        print(line)