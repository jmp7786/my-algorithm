def dfs(computers, i, visited):
    stack = [i]

    while stack:
        j = stack.pop()
        visited[j] = 1
        for y in range(len(computers)):
            if computers[j][y] == 1 and visited[y] == 0:
                stack.append(y)

def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]

    for i in range(n):
        if visited[i] == 0:
            dfs(computers, i, visited)
            answer += 1

    return answer


a = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
result = solution(3, a)

print(result)
