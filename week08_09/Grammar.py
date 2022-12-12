from ProductionSet import ProductionSet


class Grammar:

    def __init__(self, file_name):
        self.nonTerminals = []
        self.terminals = []
        self.startingSymbol = ""
        self.productionSet = ProductionSet()
        self.read_grammar_from_file(file_name)

    def read_grammar_from_file(self, file_name):
        file = open(file_name, "r")
        data = file.readlines()
        self.nonTerminals = data[0].strip()
        self.terminals = data[1].strip()
        self.startingSymbol = data[2].strip()
        for line in range(3, len(data)):
            current_line = data[line].strip()
            current_line = current_line.split('->')
            key = current_line[0]
            values = current_line[1].split(' ')
            self.productionSet.addProduction(key, values)

    def print_values(self):
        print("\n")
        print("Non terminals: ", self.nonTerminals)
        print("Terminals: ", self.terminals)
        print("Starting symbol: ", self.startingSymbol)
        print("Set of Values: ", self.productionSet.getProductionSet())
        print("Is CFG or not: ", self.productionSet.check_CFG())
        print("\n")

    @staticmethod
    def print_table(table_values):
        print('    '.join(table_values[0]))
        for i in range(1, len(table_values)):
            for j in table_values[i]:
                print(j, end='    |    ')
            print("\n")

    def create_table(self):
        table_of_values = [["Index", "Info", "Parent", "RightSibling"]]
        visited = set()
        index = 1
        table_of_values.append([index, self.startingSymbol, 0, 0])
        index += 1
        self.parse(index, self.startingSymbol, visited, table_of_values)
        self.print_table(table_of_values)

    def parse(self, index, current_symbol, visited, table_of_values):
        visited.add(current_symbol)
        if current_symbol in self.productionSet.getProductionSet().keys():
            value_list = self.productionSet.getProductionSet().get(current_symbol)
            for symbol in range(0, len(value_list)):
                if symbol - 1 >= 0 and value_list[symbol] not in self.terminals:
                    table_of_values.append([index, value_list[symbol], current_symbol, value_list[symbol - 1]])
                else:
                    table_of_values.append([index, value_list[symbol], current_symbol, 0])
                index += 1
                if value_list[symbol] not in visited:
                    self.parse(index, value_list[symbol], visited, table_of_values)
