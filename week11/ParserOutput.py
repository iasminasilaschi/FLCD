class ParserOutput:

    def __init__(self, grammar, file_name):
        self.grammar = grammar
        self.fileName = file_name

    def runParsing(self):
        self.printValues()
        self.createTable()

    def printValues(self):
        print("Non terminals: ", self.grammar.getNonTerminals())
        print("Terminals: ", self.grammar.getTerminals())
        print("Starting symbol: ", self.grammar.getStartingSymbol())
        print("Set of Values: ", self.grammar.getProductionSet())
        print("Is CFG or not: ", self.grammar.getProductionSet().getIsCFG())

    def createTable(self):
        table_of_values = [["Index", "Info", "Parent", "RightSibling"]]
        visited = set()
        index = 1
        table_of_values.append([index, self.grammar.getStartingSymbol(), 0, 0])
        index += 1
        self.parse(index, self.grammar.getStartingSymbol(), visited, table_of_values)
        self.printTableToScreen(table_of_values)
        self.printTableToFile(table_of_values)

    def parse(self, index, current_symbol, visited, table_of_values):
        visited.add(current_symbol)
        if current_symbol in self.grammar.getProductionSetKeys():
            value_list = self.grammar.getProductionSetValue(current_symbol)
            for symbol in range(0, len(value_list)):
                if symbol - 1 >= 0 and value_list[symbol] not in self.grammar.getTerminals():
                    table_of_values.append([index, value_list[symbol], current_symbol, value_list[symbol - 1]])
                else:
                    table_of_values.append([index, value_list[symbol], current_symbol, 0])
                index += 1
                if value_list[symbol] not in visited:
                    self.parse(index, value_list[symbol], visited, table_of_values)

    @staticmethod
    def printTableToScreen(table_values):
        print('    '.join(table_values[0]))
        for i in range(1, len(table_values)):
            for j in table_values[i]:
                print(j, end='    |    ')
            print("\n")

    def printTableToFile(self, table_values):
        file = open(self.fileName, "w")
        for i in range(1, len(table_values)):
            for j in table_values[i]:
                file.write(str(j))
                file.write('    |    ')
            file.write("\n")
