# Shannon Fano

values = [0.3, 0.1, 0.1, 0.2, 0.3]
letters = ['A', 'B', 'C', 'D', 'E']

nodes = []

for i in range(len(values)):
    nodes.append([letters[i], values[i], ''])

nodes.sort(key=lambda x: x[1], reverse=True)

def divList(list):
    pivoty = []
    n = len(list)

    if n == 2:
        return [list[0]], [list[1]]
    else:
        sum1 = 0.0
        sum2 = 0.0

        for i in range(1, n-1):
            left = list[:i]
            right = list[i:]
            k = len(left)

            for numb in range(0, len(left)):
                sum1 += left[numb][1]

            l = len(right)

            for numb in range(len(right)):
                sum2 += right[numb][1]

            diff = abs(sum1 - sum2)
            pivoty.append([i, diff])
            sum1, sum2 = 0.0, 0.0

        # print(pivoty)
        pivoty = sorted(pivoty, key=lambda x: x[1])
        # print(pivoty)
        axis = pivoty[0][0]
        # print(list[:axis], list[axis:])
        return list[:axis], list[axis:]




def treePath(list):
    l, r = divList(list)

    for i in l:
        i[2] += '0'
    for i in r:
        i[2] += '1'

    if len(l) == 1 and len(r) == 1:

        return
    treePath(r) and treePath(l)

    return nodes


def encode(text, nodes):
    code = ''
    for i in range(len(text)):
        for j in range(len(nodes)):
            if text[i] == nodes[j][0]:
                code += nodes[j][1]
    print(code)


def decode(code, codes):
    text = ''
    hcode = code
    while len(hcode) > 0:
        for i in range(len(codes)):
            n = (len(codes[i][1]))
            if codes[i][1] == hcode[:n]:
                text += codes[i][0]
                hcode = hcode[n:]
    print(text)

divList(nodes)
# print(5 // 2 + 1)

# print(treePath(nodes))
h_nodes = treePath(nodes)

print(h_nodes)
codes = []
for i in range (len(h_nodes)):
    codes.append([h_nodes[i][0], h_nodes[i][2]])

print(codes)

encode('ACBDE', codes)
decode('0001111110',codes)