import sys
'''
input example
123402

7755
'''

input_ = sys.stdin.readline().rstrip()
len_ = len(input_)

left = sum([int(input_[x]) for x in range(len_//2)])
right = sum([int(input_[x]) for x in range(len_//2, len_)])

if left == right:
    print("LUCKY")
else:
    print("READY")
