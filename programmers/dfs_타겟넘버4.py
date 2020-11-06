answer = 0
def spread(idx, numbers, target):
    global answer
    N = len(numbers)
    if(idx== N and target == sum(numbers)):
        answer += 1
        return
    if(idx == N):
        return

    spread(idx+1,  numbers[:], target)
    tmps = numbers[:]
    tmps[idx] *= -1
    spread(idx+1, tmps, target)
def solution(numbers, target):
    global answer
    spread(0,numbers,target)
    return answer

a = [1, 1, 1, 1, 1]
t = 3
result = solution(a, t)
print(result)

