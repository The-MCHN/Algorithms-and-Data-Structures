# Huffman

class node:
    def __init__(self, symbol, value, left=None, right=None):
        self.symbol = symbol
        self.value = value
        self.left = left
        self.right = right
        self.dirctn = ''


codes = []


def printNodes(node, code=''):
    codeN = code + str(node.dirctn)

    if (node.left):
        printNodes(node.left, codeN)
    if (node.right):
        printNodes(node.right, codeN)

    if not node.left and not node.right:
        codes.append([node.symbol, codeN])


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


# tworzenie listy w której każdy element ma przypisane dwa elementy: wartość i literę
values = [0.3, 0.1, 0.2, 0.1, 0.2, 0.1]
letters = ['A', 'B', 'C', 'D', 'E', 'F']

nodes = []

for i in range(len(values)):
    nodes.append(node(letters[i], values[i]))

# tworzenie drzewa
while len(nodes) > 1:
    nodes = sorted(nodes, key=lambda x: x.value)

    left = nodes[0]
    right = nodes[1]

    left.dirctn = 0
    right.dirctn = 1

    nNode = node(left.symbol + right.symbol, left.value + right.value, left, right)
    nodes = nodes[2:]
    nodes.append(nNode)

printNodes(nodes[0])

# print(nodes[0].right.right.right.left.value)

print()
tekst = 'BABA'

print(codes)
encode(tekst, codes)
decode('0101001010', codes)
decode('00010111', codes)

# print(codes)
