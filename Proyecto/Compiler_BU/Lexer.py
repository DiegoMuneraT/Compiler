from Table import Table

class Lexer:
    def __init__(self, table: Table):
        self.table = table
        self.stack = []

    def parse_string(self, string, parsing_table):
        action_table = parsing_table['action']
        goto_table = parsing_table['goto']
        stack = [0]
        string += '$'
        i = 0
        while True:
            state = stack[-1]
            symbol = string[i]
            if symbol not in action_table[state]:
                return False
            action, value = action_table[state][symbol]
            if value.startswith('shift'):
                stack.append(symbol)
                next_state = int(value.split(' ')[1])
                stack.append(next_state)
                i += 1
            elif value.startswith('reduce'):
                head, body = value.split(' ')[1].split('->')
                for _ in range(len(body) * 2):
                    stack.pop()
                state = stack[-1]
                stack.append(head)
                stack.append(goto_table[state][head])
            elif action == 'accept':
                return True
            else:
                return False
        
    # -----------------PARSER-----------------
    def analyze_input(self):
        parsing_table = self.table.get_parsing_table(self.table.grammar.productions)
        string = input("Ingrese la cadena: ")
        result = self.parse_string(string, parsing_table)
        # Esto es lo que no funciona, printea siempre 'no' al quitar el not del if
        if result:
            print('si se acepta')
        else:
            print('no se acepta')
    
