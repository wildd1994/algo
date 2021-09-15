import json


def max_key(graph):
    max_value = -1
    for key in graph.keys():
        if int(key) > max_value:
            max_value = int(key)
    return int(max_value)


def check(start, graph, color):
    color[start] = 1
    for item in graph[str(start)]:
        if str(item) in graph.keys():
            if color[item] == 0:
                check(item, graph, color)
            if color[item] == 1:
                return False
    color[start] = 2


def check_cycle(graph):
    n = max_key(graph)
    color = [0] * (n + 1)
    for key in graph.keys():
        if color[int(key)] == 0:
            if check(int(key), graph, color) is not None:
                return True
    return False


if __name__ == '__main__':
    with open('config.json') as file:
        dict_tmp = json.load(file)
    if check_cycle(dict_tmp):
        print('Цикл есть')
    else:
        print('Цикла нет')

