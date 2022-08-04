from copy import deepcopy
from itertools import product


def rotate_key(key):
    len_ = len(key)
    tmp = [[0] * len_ for _ in range(len_)]
    for i, j in product(range(len_), range(len_)):
        tmp[i][j] = key[j][len_ - i - 1]
    return tmp


def check_lock(lock_exp, len_):
    for i, j in product(range(len_, 2 * len_), range(len_, 2 * len_)):
        if lock_exp[i][j] != 1:
            return False
    return True


def solution(key, lock):
    len_ = len(lock)
    lock_exp = [[0]*(3*len_) for _ in range(3*len_)]
    for i in range(len_, 2*len_):
        for j in range(len_, 2*len_):
            lock_exp[i][j] = lock[i-len_][j-len_]

    for _ in range(4):
        for x, y in product(range(1, 2 * len_), range(1, 2 * len_)):
            tmp = deepcopy(lock_exp)
            for k_x, k_y in product(range(len(key)), range(len(key))):
                tmp[k_x + x][k_y + y] += key[k_x][k_y]
            if check_lock(tmp, len_):
                print(tmp)
                return True

        key = rotate_key(key)
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
