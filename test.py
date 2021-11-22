import re
variables = r"([a-zA-Z_])+(\d)*( = )+(\d|\w)*(\.+(\w)+)*(\((\d|\w)*\))*" #Validasi variabel

f = open('./test.txt', 'r')
for line in f:
  x = re.search(variables, line)
  for i in range(x.start(), x.end()):
    print(line[i], end="")
  print("")
