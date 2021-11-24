from typing import NamedTuple

class User(NamedTuple):
    name: str

class binTree(NamedTuple):
    value: str
    left: int
    right: int


def verdictCYK(token, CNFgrammar) :
    pjgToken = len(token)
    tableCYK = [[[] for i in range(pjgToken - j)] for j in range(pjgToken)]
    
    for i, word in enumerate(token):
        for rule in CNFgrammar:
            if f"'{word}'" == rule[1]:
                tableCYK[0][i].append(binTree(rule[0], word, None))
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
                print(tableCYK)
                                
    start = CNFgrammar[0][0]
    if len(token) > 0:
        final_nodes = [n for n in tableCYK[-1][0] if n.value == start]
        if final_nodes:
            verdict = "ACCEPTED"
        else:
            verdict = "SYNTAX ERROR"
    else:
        verdict = "ACCEPTED"
    return verdict
    
def CYKParser(token, CNFgrammar):
    print(token)
    n = len(token)
    m = len(CNFgrammar)

    dp = [[[0 for i in range(m + 1)] for i in range(n + 1)] for i in range(n + 1)]
    R = [None] * (m + 1)
    mp = {}
    for i, variable in enumerate(CNFgrammar):
        mp[variable] = i + 1
        R[i + 1] = CNFgrammar[variable]

    for s in range(1, n + 1):       
        for v in range(1, m + 1):   
            for e in R[v]:
                if (e[0] == token[s - 1] and len(e) == 1):
                    dp[1][s][v] = True
                    

    for l in range(2, n + 1):
        for s in range(1, (n - l + 2)):
            for p in range(1, l):
                for a in range(1, m + 1):
                    for e in R[a]:
                        if (len(e) == 2):
                            b = mp[e[0]]
                            c = mp[e[1]]
                            if (dp[p][s][b] and dp[l - p][s + p][c]):
                                dp[l][s][a] = True
    if (dp[n][1][1]):
        print("Accepted")
    else :
        print("Error")