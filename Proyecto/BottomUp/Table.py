from Grammar import Grammar

class Table:
    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.table = {}

    def create_table(self):
        tabla = {}
        productions = self.grammar.rules
        first = self.grammar.first
        Nterminals = self.grammar.Nterminals
        # print("Productions\n")
        # print(productions)
        print(self.grammar.rules)
        
        for nterminal in productions:
            tabla[nterminal] = {}
            for a in first[nterminal]:
                print(a)

                for b in productions[nterminal]:
                    if a in b:
                        tabla[nterminal][a] = b
                
                if b[0] in Nterminals:
                    if a in first[b[0]]:
                        tabla[nterminal][a] = b


            if 'epsilon' in first[nterminal]:
                for b in self.grammar.follow[nterminal]:
                    tabla[nterminal][b] = productions[nterminal]

        self.table = tabla
    
    def print_table(self):
        for left, right in self.table.items():
            print(left, right, '\n')