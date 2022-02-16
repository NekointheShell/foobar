class Morethan100Error(Exception):
    pass


def solution(data, n):
    if len(data) > 100: raise Morethan100Error()

    counter = {}
    for entry in data: counter[str(entry)] = 0
    for entry in data: counter[str(entry)] += 1

    for key,value in counter.items():
        if value > n: counter.pop(key)

    ret = []
    for entry in data:
        if str(entry) in counter: ret.append(entry)

    return ret
