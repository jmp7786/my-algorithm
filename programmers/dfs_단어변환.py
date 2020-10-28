def solution(begin, target, words):
    visited = [0 for i in range(len(words))]
    results = []
    dfs(begin, 0, target, words, visited, results)
    print(results)
    return min(results)

def dfs(word, depth, target, words, visited, results):
    if word == target:
        results.append(depth)
        return

    for i in range(len(words)):
        count = 0
        if visited[i] == 1:
            continue
        for j in range(len(word)): #단어 변경 확인
            if word[j] != words[i][j]:
                count += 1
        if count == 1:
            visited[i] = 1
            dfs(words[i], depth+1, target, words, visited, results)
            visited[i] = 0

a = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
result = solution('hit', 'cog', a)
print(result)

