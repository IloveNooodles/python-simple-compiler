# Python implementation for the
# CYK Algorithm
# from grammar.cfgtocnf import *

# Rules of the grammar
# R = mapGrammar(convertGrammar((readGrammarFile("lib/grammar/cfg.txt"))))

# Function to perform the CYK Algorithm
def cykParse(w, R):
    n = len(w)
      
    # Initialize the table
    T = [[set([]) for j in range(n)] for i in range(n)]
    # Filling in the table
    for j in range(0, n):
  
        # Iterate over the rules
        for lhs, rule in R.items():
            for rhs in rule:
                  
                # If a terminal is found
                if len(rhs) == 1 and \
                rhs[0] == w[j]:
                    T[j][j].add(lhs)

        
        for i in range(j, -1, -1):   
            
            # Iterate over the range i to j + 1   
            for k in range(i, j):  
                # Iterate over the rules
                for lhs, rule in R.items():
                    for rhs in rule:
                        # If a terminal is found
                        if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k + 1][j]:
                            T[i][j].add(lhs)
  
    # If word can be formed by rules 
    # of given grammar
    if len(T[0][n-1]) != 0:
        print("True")
    else:
        print("False")
      
# Driver Code
  
# Given string
# Function Call


if __name__ == "__main__":
  pass