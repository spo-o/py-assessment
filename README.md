# Python Rush Assessment

This repository contains my solutions for the 5 rush pattern generation tasks in python.

For all the tasks, I approached the problem by building the output row by row using nested loops. 
I first identified the corner positions since those conditions are the most specific, then handled borders separately, and finally filled the inside with spaces.

Most of the debugging and testing went into handling edge cases correctly, especially:
- 1x1
- 1xn
- nx1

For rush-1-2, I also had to carefully handle escaped backslash characters in Python.

For rush-1-3, rush-1-4, and rush-1-5, I added explicit handling for single row and single column cases because overlapping corner conditions were producing incorrect outputs initially.

The main focus throughout the assessment was keeping the logic simple, readable, and matching the expected output formatting exactly.

