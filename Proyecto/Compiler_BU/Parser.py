import re

class Parser:
    def __init__(self):
        self.rules = {}
        self.terminals = {}
        self.Nterminals = {}
        self.first = {}
        self.follow = {}
        self.start = None
        self.productions = []

    def add_rule(self, left, right):
        if left not in self.rules:
            self.rules[left] = []
        self.rules[left] += right

    def add_terminals(self, right):
        for element in right:
            if element == "epsilon":
                continue
            hlp = re.findall("[a-z0-9\+\/\*\-\%\=\(\)]", element)
            for token in hlp:
                self.terminals[token] = token

    def add_Nterminals(self, left):
        self.Nterminals[left] = left

    def add_productions(self, production):
        left, right = production.split("->")
        right = right.split("|")
        for element in right:
            self.productions.append(f"{left}->{element}")

    def item_closure(self, I, productions):
        #Se puede optimizar verificando si I está vacio.
        J = I.copy()
        while True:
            added = False
            for item in list(J):
                left, right = item.split("->")
                dot_index = right.index(".")
                if dot_index + 1 < len(right) and right[dot_index + 1] in self.Nterminals:
                    next_Nterminal = right[dot_index + 1]
                    for production in productions:
                        if production.startswith(next_Nterminal):
                            new_item = production.replace("->", "->.")
                            if new_item not in J:
                                J.append(new_item)
                                added = True
            if not added:
                break
        # print
        # (J)
        return J

    def goto(self, I, X, productions):
        new_items = []
        for item in I:
            left, right = item.split("->")
            dot_index = right.index(".")
            if dot_index + 1 < len(right) and right[dot_index + 1] == X:
                new_item = left + "->" + right[:dot_index] + X + "." + right[dot_index + 2:]
                new_items.append(new_item)
        return self.item_closure(new_items, productions)

    def get_item_set(self, productions):
        item_sets = []
        start_production = productions[0]
        start_symbol = start_production.split("->")[0]
        start_item_set = self.item_closure([f"{start_symbol}'->.{start_symbol}"], productions)
        item_sets.append(start_item_set)
        symbols = [start_symbol]
        for production in productions:
            left, right = production.split("->")
            for symbol in right:
                if symbol in symbols: continue
                symbols.append(symbol)

        while True:
            added = False
            for item_set in item_sets:
                for symbol in symbols:
                    new_item_set = self.goto(item_set, symbol, productions)
                    if new_item_set and new_item_set not in item_sets:
                        item_sets.append(new_item_set)
                        added = True
            if not added:
                break
        return item_sets

    def get_lr0_canonical(self, productions):
        start_production = productions[0]
        start_symbol = start_production.split("->")[0]
        start_state = self.item_closure([f"{start_symbol}'->.{start_symbol}"], productions)
        states = [start_state]
        transitions = []
        symbols = [start_symbol]
        for production in productions:
            left, right = production.split("->")
            for symbol in right:
                symbols.append(symbol)
        
        while True:
            added = False
            for state in states:
                for symbol in symbols:
                    new_state = self.goto(state, symbol, productions)
                    if new_state:
                        if new_state not in states:
                            states.append(new_state)
                            added = True
                        transition = (states.index(state), symbol, states.index(new_state))
                        transitions.append(transition)
            if not added:
                break
        return states, transitions


