import sys

'''
input example
K1KA5CB7
AJKDLSI412K4JSJ9D
'''

input_ = sys.stdin.readline().rstrip()
alpha_list = []
num_list = []
for x in input_:
    if x.isalpha():
        alpha_list.append(x)
    else:
        num_list.append(int(x))
alpha_list.sort()
num = sum(num_list)
print(*alpha_list, num, sep='')
