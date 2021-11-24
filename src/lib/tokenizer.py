import os
import sys 
import re

# multLine1 = r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
# multLine2 = r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

def lex(text, tokenExprs):
    pos = 0             # absolute position
    currPos = 1         # position in relative to line
    line = 1            # current line
    tokens = []

    while (pos < len(text)):
        if text[pos] == '\n':
            line += 1
            currPos = 1

        flag = None
        for tokenExpr in tokenExprs:
            pattern, tag = tokenExpr    

            # if line == 1:
            #     if pattern == multLine1:
            #         pattern = r'[^\w]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
            #     elif pattern == multLine2:
            #         pattern = r'[^\w]*[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

            regex = re.compile(pattern)
            flag = regex.match(text, pos)

            if flag:
                # texts = flag.group(0)
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not flag:
            print(f"\nSYNTAX ERROR\nIllegal character {text[pos]} at line {line} and column {currPos}")
            sys.exit(1)
        else:
            pos = flag.end(0)
        currPos += 1

    return tokens

tokenExprs = [
    # Not token
    (r'[ \t]+',                                      None),
    (r'#[^\n]*',                                     None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),
    (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',             "MULTILINE"),
    (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',             "MULTILINE"),
    (r'\n',                                          "NEWLINE"),

    # Operator
    (r'\=(?!\=)',       "EQUAL"),
    (r'\==',            "ISEQ"),
    (r'!=',             "NEQ"),
    (r'<=',             "LE"),
    (r'<',              "L"),
    (r'>=',             "GE"),
    (r'>',              "G"),
    (r'\(',             "LB"),
    (r'\)',             "RB"),
    (r'\[',             "LSB"),
    (r'\]',             "RSB"),
    (r'\{',             "LCB"),
    (r'\}',             "RCB"),
    (r'\:',             "COLON"),
    (r'-=',             "SUBTREQ"),
    (r'\*=',            "MULEQ"),
    (r'\+=',            "SUMEQ"),
    (r'/=',             "DIVEQ"),
    (r'\->',            "ARROW"),
    (r'\+',             "ADD"),
    (r'\-',             "SUBTR"),
    (r'\*',             "MUL"),
    (r'/',              "DIV"),
    (r'\,',             "COMMA"),
    (r'\w+[.]\w+',      "DOTBETWEEN"),
    (r'\.',             "DOT"),
    (r'\%',             "MOD"),

    # Type
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'\bdict\b',               "TYPE"),
    (r'\bint\b',                "TYPE"),
    (r'\bstr\b',                "TYPE"),
    (r'\bfloat\b',              "TYPE"),
    (r'\bcomplex\b',            "TYPE"),
    (r'\blist\b',               "TYPE"),
    (r'\btuple\b',              "TYPE"),

    # keyword
    (r'\band\b',                "AND"),
    (r'\bor\b',                 "OR"),
    (r'\bnot\b',                "NOT"),
    (r'\bTrue\b',               "TRUE"),
    (r'\bFalse\b',              "FALSE"),
    (r'\bNone\b',               "NONE"),
    (r'\bif\b',                 "IF"),
    (r'\belse\b',               "ELSE"),
    (r'\belif\b',               "ELIF"),
    (r'\bfor\b',                "FOR"),
    (r'\bin\b',                 "IN"),
    (r'\brange\b',              "RANGE"),
    (r'\bwhile\b',              "WHILE"),
    (r'\bbreak\b',              "BREAK"),
    (r'\bcontinue\b',           "CONTINUE"),
    (r'\bpass\b',               "PASS"),
    (r'\bfrom\b',               "FROM"),
    (r'\bimport\b',             "IMPORT"),
    (r'\bas\b',                 "AS"),
    (r'\bis\b',                 "IS"),
    (r'\bdef\b',                "DEF"),
    (r'\breturn\b',             "RETURN"),
    (r'\braise\b',              "RAISE"),
    (r'\bwith\b',               "WITH"),
    (r'\bclass\b',              "CLASS"),

    # Exception for variable
    (r'[A-Za-z_][A-Za-z0-9_]*', "VAR"),
]

def createToken(text):

    # Read file
    file = open(text, encoding="utf8")
    characters = file.read()
    file.close()

    tokens = lex(characters, tokenExprs)
    tokenResult = []

    for token in tokens:
        tokenResult.append(token)


    # Write file
    path = os.getcwd()
    fileWrite = open(path + "/result/tokenResult.txt", 'w')
    for token in tokenResult:
        fileWrite.write(str(token)+" ")
        # print(token)
    fileWrite.close()

    return tokenResult

# if __name__ == "__main__": 
#     path = os.getcwd()
#     createToken(path + "/test/inputAcc.txt")
