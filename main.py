import json


def check(start, graph, color):
    color[start] = 1
    for item in graph[str(start)]:
        if str(item) in graph.keys():
            if color[str(item)] == 0:
                check(str(item), graph, color)
            if color[str(item)] == 1:
                return False
    color[start] = 2


def check_cycle(graph):
    color = {key: 0 for key in graph.keys()}
    for key in graph.keys():
        if color[key] == 0:
            if check(key, graph, color) is not None:
                return True
    return False


if __name__ == '__main__':
    with open('config1.json') as file:
        dict_tmp = json.load(file)
    if check_cycle(dict_tmp):
        print('Цикл есть')
    else:
        print('Цикла нет')

