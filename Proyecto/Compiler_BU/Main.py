from Parser import Parser
from Table import Table
from Lexer import Lexer

def read_grammar():
    print("Ingrese la gramatica")
    grammar = Parser()
    line = input().split(" ")
    str1 = ""
    line = str1.join(line)
    while line:
        grammar.add_productions(line)
        left, right = line.split("->")
        right = right.split("|")
        if grammar.start is None:
            grammar.start = left
        grammar.add_rule(left, right)
        grammar.add_terminals(right)
        grammar.add_Nterminals(left)
        line = input().split(" ")
        str1 = ""
        line = str1.join(line)

    # grammar.create_first()
    # grammar.create_follow()
    print("Producciones: ", grammar.productions)

    # -----------------ITEMS-----------------
    # Printear los item sets
    item_sets = grammar.get_item_set(grammar.productions)
    for i, item_set in enumerate(item_sets):
        print(f"Item set {i}:")
        for item in item_set:
            print(f" {item}")

    # -----------------ESTADOS Y TRANSICIONES-----------------
    # Printear los estados y las transiciones
    states, transitions = grammar.get_lr0_canonical(grammar.productions)
    for i, state in enumerate(states):
        print(f'State {i}:')
        for item in state:
            print(f' {item}')
    print('Transitions:')
    for transition in transitions:
        print(f' {transition}')
    
    # -----------------TABLA-----------------
    table = Table(grammar)
    table.print_table()

    # -----------------LEXER-----------------
    lexer = Lexer(table)
    lexer.analyze_input()

if __name__ == "__main__":
    grammar = read_grammar()