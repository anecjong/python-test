import sys

'''
input example
0001100
'''
input_ = sys.stdin.readline().rstrip()
count = 0

for idx in range(1, len(input_)):
    if input_[idx-1] != input_[idx]:
        count += 1
print((count+1)//2)
