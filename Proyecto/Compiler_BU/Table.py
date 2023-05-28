from Parser import Parser


class Table:
    def __init__(self, grammar: Parser):
        self.grammar = grammar
        self.table = {}

    def get_parsing_table(self, productions):
        productions = self.grammar.productions
        start_production = productions[0]
        start_symbol = start_production.split('->')[0]
        states, transitions = self.grammar.get_lr0_canonical(productions)
        terminals = set()
        non_terminals = set()
        for production in productions:
            left, right = production.split('->')
            non_terminals.add(left)
            for symbol in right:
                if symbol not in non_terminals:
                    terminals.add(symbol)
        terminals.add('$')
        action = {}
        goto = {}
        for i, state in enumerate(states):
            action[i] = {}
            goto[i] = {}
            for item in state:
                left, right = item.split('->')
                dot_index = right.index('.')
                if dot_index + 1 == len(right):
                    if left == f"{start_symbol}'":
                        action[i]['$'] = ('accept', '')
                    else:
                        production_index = productions.index(f'{left}->{right[:-1]}')
                        for terminal in terminals:
                            action[i][terminal] = (f'r{production_index}', f'reduce {left}->{right[:-1]}')
                else:
                    next_symbol = right[dot_index + 1]
                    if next_symbol in terminals:
                        next_state = [j for j, s in enumerate(states) if self.grammar.goto(state, next_symbol, productions) == s][0]
                        action[i][next_symbol] = (f's{next_state}', f'shift {next_state}')
            for non_terminal in non_terminals:
                next_state = self.grammar.goto(state, non_terminal, productions)
                if next_state:
                    next_state_index = [j for j, s in enumerate(states) if s == next_state][0]
                    goto[i][non_terminal] = next_state_index
        return {'action': action, 'goto': goto}

    # -----------------TABLA-----------------
    # Printear la tabla
    def print_table(self):
        print("\nTabla:")
        parsing_table = self.get_parsing_table(self.grammar.productions)
        action_table = parsing_table['action']
        goto_table = parsing_table['goto']
        for state in sorted(action_table.keys()):
            print(f' State {state}:')
            for symbol in sorted(action_table[state].keys()):
                print(f'  action[{state}][{symbol}] = {action_table[state][symbol]}')
        for state in sorted(goto_table.keys()):
            for symbol in sorted(goto_table[state].keys()):
                print(f'  goto[{state}][{symbol}] = {goto_table[state][symbol]}')