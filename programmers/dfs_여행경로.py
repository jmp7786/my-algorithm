answer = None


def findway(passes, tickets):
    if not tickets:
        global answer
        if not answer:
            answer = passes

    for i, v in enumerate(tickets):
        if passes[-1] == v[0]:
            findway(passes + [v[1]], tickets[:i] + tickets[i + 1:])


def solution(tickets):
    tickets.sort()
    findway(["ICN"], tickets)

    global answer
    print(answer)
    return answer
a = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]

solution()