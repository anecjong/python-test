import sys

s = "aabbaccc"
s = "ababcdcdababcdcd"

def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[:step]
        count = 1
        for idx in range(step, len(s), step):
            if prev == s[idx:idx+step]:
                count += 1
            else:
                compressed += (str(count) + prev) if count >=2 else prev
                prev = s[idx:idx+step]
                count = 1
        compressed += (str(count) + prev) if count >=2 else prev
        answer = min(answer, len(compressed))

    return answer
