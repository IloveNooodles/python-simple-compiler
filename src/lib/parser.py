def cykParse(w, R):
    n = len(w)
    T = [[set([]) for j in range(n)] for i in range(n)]
    for j in range(0, n):
      for lhs, rule in R.items():
        for rhs in rule:    
          if len(rhs) == 1 and rhs[0] == w[j]:
            T[j][j].add(lhs)

      
      for i in range(j, -1, -1):     
        for k in range(i, j):  
          for lhs, rule in R.items():
            for rhs in rule:
              if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k + 1][j]:
                T[i][j].add(lhs)
  
    if 'S' in T[0][n-1]:
        print("Compiled Successfully :)")
    else:
        print("Compile Failed :(")
      
if __name__ == "__main__":
  pass