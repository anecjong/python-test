import sys
from itertools import product

input_ = sys.stdin.readline()
row_ = ord(input_[0]) - ord('a') + 1
col_ = int(input_[1])

move_1 = [2, -2]
move_2 = [1, -1]

count = 0

for i, j in product(move_1, move_2):
    if 1 <= (row_ + i) <= 8 and 1 <= (col_+j) <= 8:
        count += 1
for j, i in product(move_1, move_2):
    if 1 <= (row_ + i) <= 8 and 1 <= (col_+j) <= 8:
        count += 1
print(count)
