import sys
import re
import heapq

def initialize_graph():
    graph = {}
    edge_list = read_file()
    for edge_inf in edge_list:
        node1 = edge_inf.split(',')[0]
        node2 = edge_inf.split(',')[1]
        cost = int(edge_inf.split(',')[2])
        # ノードの設定と無向エッジの設定
        graph = set_new_node(graph, node1, node2)
        graph[node1][node2] = cost
        graph[node2][node1] = cost
    return graph

def read_file():
    file_name = 'edge_inf.csv'
    edge_list = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            edge_list.append(re.sub(r'[\r\n]', '', line))
    return edge_list

def set_new_node(graph, node1, node2):
    if not node1 in graph.keys():
        graph[node1] = {}
    if not node2 in graph.keys():
        graph[node2] = {}
    return graph

def solve_by_dijkstra(graph):
    # ノード毎のSTARTからの最小コスト
    min_dist_dict = {}
    # ノードに最小コストで辿り着く場合の直前のノード
    prev_node_dict = {}
    q = []
    heapq.heappush(q, (0, 'START'))

    prev_node = ''

    while True:
        # 確定したノードから遷移可能なノードのうち
        # 最小のコストと遷移先ノードをmin_dist_dictとprev_node_dictに設定
        dist, node = heapq.heappop(q)
        min_dist_dict[node] = dist
        prev_node_dict[node] = prev_node
        # もしGOALノードの最小コストが確定したらループを抜ける
        if node == 'GOAL':
            return min_dist_dict, prev_node_dict
        prev_node = node
        # 確定したノードから遷移可能なノードについて
        # コストを計算し、キュー(q)に追加する
        culc_min_dist_and_put(graph, q, node, min_dist_dict, prev_node_dict)

def culc_min_dist_and_put(graph, q, departure_node, min_dist_dict, prev_node_dict):
    # 直前に確定したノードから遷移可能なすべてのノードについて繰り返し
    for arrival_node in graph[departure_node].keys():
        # 遷移可能なノードについて、直前に確定したノードから遷移した場合のコストを計算
        tmp_d = min_dist_dict[departure_node] + graph[departure_node][arrival_node]
        # 過去に遷移先ノードの最小コストを計算済みかどうか
        if arrival_node in min_dist_dict.keys():
            # 過去に計算していたSTARTからの最小コストより直前に確定したノードから遷移した場合の
            # コストのほうが小さかった場合、最小コストを更新
            if tmp_d < min_dist_dict[arrival_node]:
                min_dist_dict[arrival_node] = tmp_d
                heapq.heappush(q, (min_dist_dict[arrival_node], arrival_node))
        else:
            min_dist_dict[arrival_node] = tmp_d
            heapq.heappush(q, (min_dist_dict[arrival_node], arrival_node))

if __name__ == "__main__":
    graph = initialize_graph()
    min_dist_dict, prev_node_dict = solve_by_dijkstra(graph)
    print('Route: GOAL', end='')
    node = 'GOAL'
    while True:
        if node == 'START':
            print()
            break
        print(' ←' + prev_node_dict[node], end='')
        node = prev_node_dict[node]
    print('Min Coast: ' + str(min_dist_dict['GOAL']))
