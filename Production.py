# expected_format = '[([(s1, out, 1, 2, 3), (ai, out, 1, 2)], [(0, A, M, in), (0, A, N, out)]), ' \
#     '([(s1, out, 1, 2, 3), (ai, out, 1, 4)], [(0, A, M, in), (0, A, N, out)]), ' \
#     '([(s1, out, 1, 2, 5), (ai, out, 1, 6)], [(0, A, M, in), (0, A, N, out)])]'

class Production:
    def __init__(self, left_graph, right_graph, attachment):
        self.operations = []
        self.left_graph = left_graph
        self.right_graph = right_graph
        self.attachment = attachment

    def get_rl_graphs(self):
        return self.left_graph, self.right_graph

    @staticmethod
    def if_input_is_valid(input_data) -> bool:
        S = input_data.replace('\n', '\n ')
        S = S.split(' ')
        print(S)
        flag = True
        if len(S) % 4 != 0:
            return False
        for i in range(len(S)):
            if (i + 1) % 4 != 0 and S[i][-1] != ',':
                flag = False
                break
            if (i + 1) % 4 == 0 and i < len(S) - 1 and S[i][-2:] != ";\n":
                flag = False
                break
        return flag

    # input format:
    # """edge_label, direction, index_left; ver_right_label, ver_g_label, edge_label, direction;
    # edge_label, direction, index_left; ver_right_label, ver_g_label, edge_label, direction;"""
    # format after parse:
    # [[[edge_label, direction, index_left], [ver_right_label, ver_g_label, edge_label, direction]],
    # [[edge_label, direction, index_left], [ver_right_label, ver_g_label, edge_label, direction]]]
    @staticmethod
    def parse(input_data: str):
        S = input_data[:-1]
        S = S.replace('\n', ' ')
        S = S.split('; ')
        for i in range(len(S)):
            S[i] = S[i].split(', ')
        V = [[]]
        idx = 0
        idxV = 0
        while idx < len(S):
            if len(S[idx]) == 3 and idx > 0:
                V.append([])
                idxV += 1
            V[idxV].append(S[idx])
            idx += 1
        if len(V) == 0:
            return []
        return [[(operation[0][0], operation[0][1], int(operation[0][2]))] + \
                [(added_edge_desc[0], added_edge_desc[1], added_edge_desc[2], added_edge_desc[3])
                 for added_edge_desc in operation[1:]] for operation in V]

# if __name__ == '__main__':
#     Prod = Production()
#     Prod.parseProduction(expected_format)
#     for op in Prod.operations:
#         print(op)
