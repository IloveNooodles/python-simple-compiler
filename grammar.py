RULE_DICT = {}

def print_grammar(grammar):
	for rule in grammar:
		print(rule[0], " -> ", end='')
		for i in rule[1:]:
			print(i, end=' ')
		print()

def write_grammar(grammar):
    file = open('cnf_grammar.txt', 'w')
    for rule in grammar:
        file.write(rule[0])
        file.write(" -> ")
        for i in rule[1:]:
            file.write(i)
            file.write(" ")
        file.write("\n")
    file.close()

def read_grammar(grammar_file):

    with open(grammar_file) as cfg:
        baris = cfg.readlines()
    return [x.replace("->", "").split() for x in baris]

def add_rule(rule):
 
    global RULE_DICT

    if rule[0] not in RULE_DICT:
        RULE_DICT[rule[0]] = []
    RULE_DICT[rule[0]].append(rule[1:])

def convert_grammar(grammar):

    global RULE_DICT

    unit_productions, res = [], []
    index = 0

    for rule in grammar:
        new_rules = []
        if len(rule) == 2 and rule[1][0] != "'":
            unit_productions.append(rule)
            add_rule(rule)
            continue
        elif len(rule) > 2:
            terminals = [(item, i) for i, item in enumerate(rule) if item[0] == "'"]
            if terminals:
                for item in terminals:
                    rule[item[1]] = f"{rule[0]}{str(index)}"
                    new_rules += [f"{rule[0]}{str(index)}", item[0]]
                index += 1
            while len(rule) > 3:
                new_rules.append([f"{rule[0]}{str(index)}", rule[1], rule[2]])
                rule = [rule[0]] + [f"{rule[0]}{str(index)}"] + rule[3:]
                index += 1
        if rule:
        	add_rule(rule)
        	res.append(rule)
        if new_rules:
        	for i in range(len(new_rules)):
           		res.append(new_rules[i])

    while unit_productions:
        rule = unit_productions.pop()
        if rule[1] in RULE_DICT:
            for item in RULE_DICT[rule[1]]:
                new_rule = [rule[0]] + item
                if len(new_rule) > 2 or new_rule[1][0] == "'":
                    res.append(new_rule)
                else:
                    unit_productions.append(new_rule)
                add_rule(new_rule)
    return res

if __name__ == '__main__':

    write_grammar(convert_grammar(read_grammar('grammar.txt')))