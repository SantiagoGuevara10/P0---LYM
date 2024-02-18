from tokens import tokenize

def parse_defvar(tokens):
    if len(tokens) != 5:
        return False  
    if tokens[0].type == "LPAREN" and tokens[1].type == "DEFVAR" and tokens[2].type == "NAME" and tokens[3].type == "NUMBER" and tokens[4].type == "RPAREN":
        return True  
    else:
        return False  
    
def parse_assignment(tokens):
    if len(tokens) == 5 and tokens[0].type == "LPAREN" and tokens[1].type == "NAME" and tokens[2].type == "NAME" and tokens[3].type == "NUMBER" and tokens[4].type == "RPAREN":
        return True
    else:
        return False

def parse_move(tokens):
    if len(tokens) == 4 and tokens[0].type == "LPAREN" and tokens[1].type == "MOVE" and tokens[2].type == "NUMBER" and tokens[3].type == "RPAREN":
        return True
    else:
        return False

def parse_skip(tokens):
    if len(tokens) == 4 and tokens[0].type == "LPAREN" and tokens[1].type == "SKIP" and tokens[2].type == "NUMBER" and tokens[3].type == "RPAREN":
        return True
    else:
        return False

def parse_turn(tokens):
    if len(tokens) == 4 and tokens[0].type == "LPAREN" and tokens[1].type == "TURND" and tokens[2].type == "COLON" and tokens[3].type in [":left", ":right", ":around"] and tokens[4].type == "RPAREN":
        return True
    else:
        return False

def parse_face(tokens):
    if len(tokens) == 4 and tokens[0].type == "LPAREN" and tokens[1].type == "FACE0" and tokens[2].type == "COLON" and tokens[3].type in [":north", ":south", ":east", ":west"] and tokens[4].type == "RPAREN":
        return True
    else:
        return False

def parse_put(tokens):
    if len(tokens) == 5 and tokens[0].type == "LPAREN" and tokens[1].type == "PUT" and tokens[2].type == "COLON" and tokens[3].type  == "MYCHIPS" or "MYBALLOONS"  and tokens[4].type == "NUMBER" and tokens[5].type == "RPAREN":
        return True
    else:
        return False

def parse_pick(tokens):
    if len(tokens) == 5 and tokens[0].type == "LPAREN" and tokens[1].type == "PICK" and tokens[2].type == "COLON" and tokens[3].type in [":balloons", ":chips"] and tokens[4].type == "NUMBER" and tokens[5].type == "RPAREN":
        return True
    else:
        return False

def parse_movedir(tokens):
    if len(tokens) == 6 and tokens[0].type == "LPAREN" and tokens[1].type == "MOVEDIR" and tokens[2].type == "NUMBER" and tokens[3].type == "COLON" and tokens[4].type in [":front", ":right", ":left", ":back"] and tokens[5].type == "RPAREN":
        return True
    else:
        return False

def parse_rundirs(tokens):
    if len(tokens) >= 5 and tokens[0].type == "LPAREN" and tokens[1].type == "RUNDIR" and all(token.type in [":front", ":right", ":left", ":back"] for token in tokens[2:-2]) and tokens[-1].type == "RPAREN":
        return True
    else:
        return False

def parse_moveface(tokens):
    if len(tokens) == 6 and tokens[0].type == "LPAREN" and tokens[1].type == "MOVEFACE" and tokens[2].type == "NUMBER" and tokens[3].type == "COLON" and tokens[4].type in [":north", ":south", ":west", ":east"] and tokens[5].type == "RPAREN":
        return True
    else:
        return False
def parse_not(tokens):
    if len(tokens) == 4 and tokens[0].type == "LPAREN" and tokens[1].type == "NOT" and tokens[2].type == "COND" and tokens[3].type == "RPAREN":
        return True
    else:
        return False
def parse_can_move(tokens):
    if len(tokens) == 5 and tokens[0].type == "LPAREN" and tokens[1].type == "CANMOVE" and tokens[2].type == "COLON" and tokens[3].type in [":north", ":south", ":east", ":west"] and tokens[4].type == "RPAREN":
        return True
    else:
        return False
        
def parse_if(tokens):
    if len(tokens) >= 7 and tokens[0].type == "LPAREN" and tokens[1].type == "IF" and tokens[2].type == "LPAREN":
        # Encontrar el índice del primer RPAREN después de la condición
        index = 3
        count = 1
        while count > 0:
            if tokens[index].type == "LPAREN":
                count += 1
            elif tokens[index].type == "RPAREN":
                count -= 1
            index += 1
        
        # Verificar si hay una rama "sino"
        has_else = tokens[index].type == "LPAREN"
        
        # Comprobar la estructura de la rama "entonces"
        if has_else:
            if tokens[index+1].type == "LPAREN":
                return True
            else:
                return False
        else:
            if tokens[index].type == "LPAREN":
                return True
            else:
                return False
    else:
        return False
    

def parse_instruction(tokens):
    if len(tokens) > 0 and tokens[0].type == "LPAREN":
        if len(tokens) > 1:
            if tokens[1].type == "=":
                return parse_assignment(tokens)
            elif tokens[1].type == "MOVE":
                return parse_move(tokens)
            elif tokens[1].type == "SKIP":
                return parse_skip(tokens)
            elif tokens[1].type == "TURND":
                return parse_turn(tokens)
            elif tokens[1].type == "FACE0":
                return parse_face(tokens)
            elif tokens[1].type == "PUT":
                return parse_put(tokens)
            elif tokens[1].type == "PICK":
                return parse_pick(tokens)
            elif tokens[1].type == "MOVEDIR":
                return parse_movedir(tokens)
            elif tokens[1].type == "RUNDIR":
                return parse_rundirs(tokens)
            elif tokens[1].type == "MOVEFACE":
                return parse_moveface(tokens)
            elif tokens[1].type == "DEFVAR":
                return parse_defvar(tokens)
            elif tokens[1].type == "NOT":
                return parse_not(tokens)
            elif tokens[1].type == "IF":
                return parse_if(tokens)
            elif tokens[1].type == "CANMOVE":
                return parse_can_move(tokens)
        return False
    else:
        return False
    
with open('exp.txt', 'r') as file:
    lines = file.readlines()

# Lista para almacenar los resultados
results = []

# Tokeniza y analiza cada línea
for line in lines:
    tokens = tokenize(line)
    result = parse_instruction(tokens)
    results.append(result)

# Comprueba si todos los resultados son True
if all(results):
    print("True")
else:
    print("False")  

    
commands_parsers = {
    'DEFVAR': parse_defvar,
    'ASSING': parse_assignment,
    'MOVE': parse_move,
    'SKIP' : parse_skip,
    'FACE': parse_face,
    'PUT' :  parse_put,
    'MOVE_FACE' : parse_moveface,
    'RUN_DIRS': parse_rundirs,
    'PICK' : parse_pick,
    'NULL': 0
    }