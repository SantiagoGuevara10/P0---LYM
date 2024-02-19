import ply.lex as lex



tokens = ["LPAREN", "RPAREN", "DEFVAR", "VAR", "NAME", "MOVE", "SKIP", "TURND", "FACE0", "PUT", "PICK", "MOVEDIR", "RUNDIR",
    "MOVEFACE", "NULL", "DIM", "MYXPOS", "MYYPOS", "MYCHIPS", "MYBALLOONS", "BALLOONSHERE", "CHIPSHERE", "SPACES", "IF", "LOOP", "REPEAT", "DEFUN", "FACING", "BLOCKED", "CANPUT",
    "CANPICK", "CANMOVE", "ISZERO", "NOTCOND", "NUMBER", "RUN", "DROP", "LEFT", "RIGHT", "DOWN", "UP" , "COLON" , "DIRECTION", "BALLOONS", "SELECT", 
    "CHIPS"]

reserved = {
    "if": "IF",
    "loop": "LOOP",
    "repeat": "REPEAT",
    "defvar": "DEFVAR",
    "move": "MOVE",
    "skip": "SKIP",
    "turn": "TURND",
    "face": "FACE0",
    "put": "PUT",
    "pick": "PICK",
    "move-dir": "MOVEDIR",
    "run-dir": "RUNDIR",
    "moveface": "MOVEFACE",
    "null": "NULL",
    "defun": "DEFUN",
    "facing?": "FACING",
    "blocked?": "BLOCKED",
    "can-put?": "CANPUT",
    "can-pick?": "CANPICK",
    "can-move?": "CANMOVE",
    "iszero?": "ISZERO"        
}




t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r'\:'
t_ignore = ' \t'

def t_SELECT(t):
    r"chips|balloons"
    return t 

def t_DIRECTION(t):
    r'(left|right|up|front|back|down|around)'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'NAME')  
    return t

def t_DEFVAR(t):
    r'defvar\s+[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NAME(t):
    r"[a-zA-Z]+"
    return t 

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_MOVE(t):
    r"move\s*\(\s*\d+\s*\)"
    return t

def t_SKIP(t):
    r"skip\s*\(\s*\d+\s*\)"
    return t

def t_TURND(t):
    r"turn\s*\(\s*:\w+\s*\)"
    return t

def t_FACE0(t):
    r"face\s*\(\s*:\w+\s*\)"
    return t


def t_FACING(t):
    r"\(facing\?\s(:north|:south|:east|:west)\)"
    return t

def t_BLOCKED(t):
    r"\(blocked\?\)"
    return t


def t_PUT(t):
    r"put\s*\(\s*:\w+\s*\d+\s*\)"
    return t

def t_PICK(t):
    r"pick\s*\(\s*:\w+\s*\d+\s*\)"
    return t

def t_CANPUT(t):
    r"can-put\?\s*\(\s*:\w+\s*\)"
    return t

def t_CANPICK(t):
    r"can-pick\?\s*\(\s*:\w+\s*\)"
    return t

def t_CANMOVE(t):
    r"can-move\?\s*\(\s*:\w+\s*\)"
    return t
def t_NOT(t):
    r"not\s*\(\s*:\w+\s*\)"
    return t

def t_MOVEDIR(t):
    r"move-dir\s*\(\s*:\w+\s*\d+\s*\)"
    return t

def t_RUNDIR(t):
    r"run-dirs\s*\(\s*(?::\w+\s*)+\)"
    return t

def t_MOVEFACE(t):
    r"move-face\s*\(\s*\d+\s*:\w+\s*\)"
    return t


def t_NULL(t):
    r"null"
    return t

def t_DIM(t):
    r"dim\s+\d+"
    return t

def t_MYYPOS(t):
    r"myypos"
    return t

def t_MYXPOS(t):
    r"myxpos"
    return t


def t_MYCHIPS(t):
    r"chips"
    return t

def t_MYBALLOONS(t):
    r"balloons"
    return t

def t_BALLOONSHERE(t):
    r"balloonshere"
    return t

def t_CHIPSHERE(t):
    r"chipshere"
    return t


def t_SPACES(t):
    r"spaces\s+\d+"
    return t


def t_IF(t):
    r"if\s+\([^\)]+\)"
    return t

def t_LOOP(t):
    r"loop\s+\([^\)]+\)"
    return t

def t_REPEAT(t):
    r"repeat\s+\d+\s+\([^\)]+\)"
    return t


def t_DEFUN(t):
    r"defun\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\([^\)]*\)"
    return t


def t_ISZERO(t):
    r"iszero\s+\([^\)]+\)"
    return t


def t_NOTCOND(t):
    r"notcond\s+\([^\)]+\)"
    return t


def t_RUN(t):
    r"run\s+[a-zA-Z_][a-zA-Z0-9_]*"
    return t


def t_DROP(t):
    r"drop\s+\(:balloons|:chips\)"
    return t

def t_DIRECTIONS(t):
    r":front|:left|:right|:back"
    return t

def t_error(t):
    t.lexer.skip(1)  

def t_newline(t):
    r'\n+'
    
    t.lexer.lineno += len(t.value)

lexer = lex.lex()
def tokenize (input_text):
    lexer.input(input_text)
    tokens = []
    while True:
        toke = lexer.token()
        if not toke:
            break
        tokens.append(toke)
    return tokens
