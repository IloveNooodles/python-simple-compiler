import keyword

terminal = keyword.kwlist

ruleDict = {}

#Read txt
def readGrammarFile(file):
  with open(file) as cfg_file:
    baris = cfg_file.readlines()
    barisConverted = []
    for i in range(len(baris)):
      splitBaris = baris[i].replace("->", "").split()
      barisConverted.append(splitBaris)
  return barisConverted

#Print read files
def printGrammar(grammar):
  for grammarRule in grammar:
    for i in range(len(grammarRule)):
      if i == 0:
        print(grammarRule[i], " -> ", end='')
      else:
        print(grammarRule[i], end=' ')
    print("\n")

#Adding rule to global var
def addGrammarRule(rule):
  global ruleDict
  
  if rule[0] not in ruleDict:
    ruleDict[rule[0]] = []
  ruleDict[rule[0]].append(rule[1:])

def convertGrammar(grammar):
    global ruleDict
    idx = 0
    unitProductions, res = [], []
    for rule in grammar:
      new_rules = []
      # buat yang cuma satu nonterminal/terminal di kanan
      if len(rule) == 2 and not rule[1][0].islower() :
        unitProductions.append(rule)
        addGrammarRule(rule)
        continue
      # Proses if lebih dari 3 nonterminalnya ini bakal di split jadi cuma 3 doang  
      while len(rule) > 3:
        
        new_rules.append([f"{rule[0]}{idx}", rule[1], rule[2]])
        rule = [rule[0]] + [f"{rule[0]}{idx}"] + rule[3:]
        idx += 1
      if rule:
        addGrammarRule(rule)
        res.append(rule)
      if new_rules:
        for i in range(len(new_rules)):
          res.append(new_rules[i])

    # Proses cuma yang ada 1 non terminal di kanan
    while unitProductions:
      rule = unitProductions.pop() 
      if rule[1] in ruleDict:
        for item in ruleDict[rule[1]]:
          new_rule = [rule[0]] + item
          # nonterminal dikanan bakal dirubah either kalo panjangnya 3 / ada terminal
          if len(new_rule) > 2 or new_rule[1][0].islower():
            res.append(new_rule)
          #Kalo cuma 2 tp dia bukan terminal masukin lg ke production ujungnya bakal dirubah jadi terminal
          else:
            unitProductions.append(new_rule)
          addGrammarRule(new_rule)
    return res

def mapGrammar(grammar):
  lenGrammar = len(grammar)
  mp = {}
  for rule in grammar :
    mp[str(rule[0])] = []
  for rule in grammar :
    elm = []
    for idxRule in range(1, len(rule)) :
      apd = rule[idxRule]
      elm.append(apd)
    mp[str(rule[0])].append(elm)
  return mp

def writeGrammar(grammar):
    file = open('cnf.txt', 'w')
    for rule in grammar:
        file.write(rule[0])
        file.write(" -> ")
        for i in rule[1:]:
            file.write(i)
            file.write(" ")
        file.write("\n")
    file.close()

if __name__ == "__main__":
  writeGrammar(convertGrammar((readGrammarFile("cfg.txt")))) 