class binTree:
    def __init__(self, value, left, right=None):
        self.value = value
        self.left = left
        self.right = right 

def verdictCYK(token, CNFgrammar) :
    pjgToken = len(token)
    tableCYK = [[[] for i in range(pjgToken - j)] for j in range(pjgToken)]
    
    for i, word in enumerate(token):
        for rule in CNFgrammar:
            if f"'{word}'" == rule[1]:
                tableCYK[0][i].append(binTree(rule[0], word))

    for words_to_consider in range(2, pjgToken + 1):
            for starting_cell in range(0, pjgToken - words_to_consider + 1):
                for left_size in range(1, words_to_consider):
                    right_size = words_to_consider - left_size

                    left_cell = tableCYK[left_size - 1][starting_cell]
                    right_cell = tableCYK[right_size - 1][starting_cell + left_size]

                    for rule in CNFgrammar:
                        left_nodes = [n for n in left_cell if n.value == rule[1]]
                        if left_nodes:
                            right_nodes = [n for n in right_cell if n.value == rule[2]]
                            tableCYK[words_to_consider - 1][starting_cell].extend(
                                [binTree(rule[0], left, right) for left in left_nodes for right in right_nodes])
                                
    start = CNFgrammar[0][0] #Simbol pertama di grammar CNF
    if len(token) > 0:
        final_nodes = [n for n in tableCYK[-1][0] if n.value == start]
        if final_nodes:
            verdict = "ACCEPTED"
        else:
            verdict = "SYNTAX ERROR"
    else:
        verdict = "ACCEPTED"
    return verdict
    