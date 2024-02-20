from tokens import tokenize

def parse_defvar(tokens):
    if len(tokens) != 5:
        return False  
    if tokens[0].type == "LPAREN" and tokens[1].type == "DEFVAR" and tokens[2].type == "NAME" and tokens[3].type == "NUMBER" and tokens[4].type == "RPAREN":
        return True  
    else:
        return False

def parse_defun(tokens):
   
    if len(tokens) < 7:
        return False
   
    if tokens[0].type != "LPAREN" or tokens[1].type != "DEFUN" or tokens[2].type != "NAME" or tokens[3].type != "LPAREN":
        return False
    
    params_end_idx = 4
    while params_end_idx < len(tokens) and tokens[params_end_idx].type != "RPAREN":
        if tokens[params_end_idx].type != "NAME":  
            return False
        params_end_idx += 1
    if params_end_idx >= len(tokens):  
        return False
   
    if params_end_idx + 2 >= len(tokens) or tokens[params_end_idx + 1].type != "LPAREN":
        return False
    
    if tokens[-1].type != "RPAREN":
        return False
    

    return True  

def parse_function_call(tokens):
    if len(tokens) < 4:  
        return False
    if tokens[0].type != "LPAREN" or tokens[1].type != "NAME" or tokens[-1].type != "RPAREN":
        return False
    
    for param in tokens[2:-1]:
        if param.type not in ["NAME", "NUMBER", "STRING"]: 
            return False
    return True  


    
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
    if len(tokens) == 5 and tokens[0].type == "LPAREN" and tokens[1].type == "TURND" and tokens[2].type == "COLON" and tokens[3].type =="DIRECTION" and tokens[4].type == "RPAREN":
        return True
    else:
        return False

def parse_face(tokens):
    if len(tokens) == 4 and tokens[0].type == "LPAREN" and tokens[1].type == "FACE0"  and tokens[2].type == "TURND" and tokens[3].type == "RPAREN":
        return True
    else:
        return False

def parse_put(tokens):
    if len(tokens) == 6 and tokens[0].type == "LPAREN" and tokens[1].type == "PUT" and tokens[2].type == "COLON" and tokens[3].type  == "SELECT"   and tokens[4].type == "NUMBER" and tokens[5].type == "RPAREN":
        return True
    else:
        return False

def parse_pick(tokens):
    if len(tokens) == 6 and tokens[0].type == "LPAREN" and tokens[1].type == "PICK" and tokens[2].type == "COLON" and tokens[3].type  and tokens[4].type == "NUMBER" and tokens[5].type == "RPAREN":
        return True
    else:
        return False

def parse_movedir(tokens):
    if len(tokens) == 6 and tokens[0].type == "LPAREN" and tokens[1].type == "MOVEDIR" and tokens[2].type == "NUMBER" and tokens[3].type == "COLON" and tokens[4].type == "DIRECTION" and tokens[5].type == "RPAREN":
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
        
        index = 3
        count = 1
        while count > 0:
            if tokens[index].type == "LPAREN":
                count += 1
            elif tokens[index].type == "RPAREN":
                count -= 1
            index += 1
        
        
        has_else = tokens[index].type == "LPAREN"
        
        
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
            command_type = tokens[1].type
            
            if command_type == "=":
                return parse_assignment(tokens)
            elif command_type == "MOVE":
                return parse_move(tokens)
            elif command_type == "SKIP":
                return parse_skip(tokens)
            elif command_type == "TURND":
                return parse_turn(tokens)
            elif command_type == "FACE0":
                return parse_face(tokens)
            elif command_type == "PUT":
                return parse_put(tokens)
            elif command_type == "PICK":
                return parse_pick(tokens)
            elif command_type == "MOVEDIR":
                return parse_movedir(tokens)
            elif command_type == "RUNDIR":
                return parse_rundirs(tokens)
            elif command_type == "MOVEFACE":
                return parse_moveface(tokens)
            elif command_type == "DEFVAR":
                return parse_defvar(tokens)
            elif command_type == "NOT":
                return parse_not(tokens)
            elif command_type == "IF":
                return parse_if(tokens)
            elif command_type == "CANMOVE":
                return parse_can_move(tokens)
           
            elif command_type == "DEFUN":
                return parse_defun(tokens)
            else:
                return False  
        else:
            return False 
    else:
        return False  
    
with open('exp.txt', 'r') as file:
    lines = file.readlines()


results = []


for line in lines:
    tokens = tokenize(line)
    result = parse_instruction(tokens)
    
    results.append(result)


if all(results):
    print("YES")
else:
    print("NO")  

    
commands_parsers = {
    'DEFVAR': parse_defvar,
    'ASSING': parse_assignment,
    'MOVE': parse_move,
    'SKIP' : parse_skip,
    'FACE': parse_face,
    'PUT' :  parse_put,
    'MOVE_FACE' : parse_moveface,
    'RUN_DIRS': parse_rundirs,
    'PICK' : parse_pick
    }