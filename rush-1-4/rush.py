import sys

def rush(x, y):

    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    # single row
    if y == 1:
        print("B" * x)
        return

    # single column
    if x == 1:
        for _ in range(y):
            print("B")
        return

    for row in range(y):

        line = ""

        for col in range(x):

            if col == 0 and (row == 0 or row == y - 1):
                line += "A"

            elif col == x - 1 and (row == 0 or row == y - 1):
                line += "C"

            elif row == 0 or row == y - 1:
                line += "B"

            elif col == 0 or col == x - 1:
                line += "B"

            else:
                line += " "

        print(line)

