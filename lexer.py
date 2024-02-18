import ply.lex as lex
from tokens import tokenize
import tokens as tk

from parse import parse_instruction
lexer = lex.lex()
def tokenFile(frase):
    tokens_line=[]

    lexer.input(frase)
    for t  in lexer:
        tokens_line.append(t.type)
    return tokens_line

def readFile(file_name:str):
    all_phrases=[]
    phrases=[]
    file= open(file_name,"r",encoding="utf-8")

    line=file.readline()


    while line !="":
        line =line.replace("\n","")
        line=line.lower()
        phrases.append(line)
        line= file.readline()
    file.close()

    i=0
    bool_parser=True

    while i <len(phrases) and bool_parser:
        tokened_phrase=tokenFile(phrases[i])
        all_phrases.append(tokened_phrase)
        i+=1
    return all_phrases


with open('exp.txt', 'r') as file:
        ejemplos = file.readlines()
    

#Tokeniza cada ejemplo y decide qué función de análisis usar
for ejemplo in ejemplos:
    tokens = tk.tokenize(ejemplo)
    print(tokens)
    resultado = parse_instruction(tokens)
    print(resultado)
    
