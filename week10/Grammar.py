from week10.ProductionSet import ProductionSet


class Grammar:

    def __init__(self, file_name):
        self.non_terminals = []
        self.terminals = []
        self.starting_symbol = ""
        self.production_set = ProductionSet()
        self.read_file(file_name)

    def read_file(self, file_name):
        file = open(file_name, "r")
        data = file.readlines()
        self.non_terminals = data[0].strip()
        self.terminals = data[1].strip()
        self.starting_symbol = data[2].strip()
        for line in range(3, len(data)):
            current_line = data[line].strip()
            current_line = current_line.split(' ::= ')
            key = current_line[0]
            # current_line[1] = current_line[1].replace(" |", '', -1)
            values = current_line[1].split(' | ')
            self.production_set.addProduction(key, values)

    def getNonTerminals(self):
        return self.non_terminals

    def getTerminals(self):
        return self.terminals

    def getStartingSymbol(self):
        return self.starting_symbol

    def getProductionSet(self):
        return self.production_set

    def getProductionSetKeys(self):
        return self.production_set.getKeys()

    def getProductionSetValue(self, key):
        return self.production_set.getValue(key)
