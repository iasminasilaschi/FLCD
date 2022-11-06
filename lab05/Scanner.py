from lab05.HashTable import HashTable


class Scanner:
    symbol_table = HashTable(10)
    constants_table = HashTable(10)
    lexical_errors = []

    characters_table = HashTable(10)
    separator_table = HashTable(10)
    operators_table = HashTable(10)
    keywords_table = HashTable(10)

    last_character_position = 62
    last_operator_position = 74
    last_separator_position = 83
    last_keyword_position = 102

    def __init__(self):
        self.populate_tables()

    def populate_tables(self):
        file = open('C://Users//Iasmina//PycharmProjects//FLCD//lab05//token.in', 'r')
        position = 0
        for line in file:
            if position < self.last_character_position:
                self.characters_table.add(line.strip())
            elif position < self.last_operator_position:
                self.operators_table.add(line.strip())
            elif position < self.last_separator_position:
                if line.strip() == 'space':
                    self.separator_table.add(' ')
                else:
                    self.separator_table.add(line.strip())
            elif position < self.last_keyword_position:
                self.keywords_table.add(line.strip())
            position += 1

    def scan(self, program):
        file = open(program, 'r')
        self.symbol_table = HashTable(10)
        self.constants_table = HashTable(10)
        self.lexical_errors = []

        line_index = 1
        all_tokens = []

        for line in file:
            part_index = 1
            tokens = self.tokenize(line)
            for token in tokens:
                if self.separator_table.contains(token) or \
                        self.operators_table.contains(token) or \
                        self.keywords_table.contains(token):
                    all_tokens.append((token, (-1, -1)))
                else:
                    try:
                        if self.valid_symbol(token):
                            self.symbol_table.add(token)
                            all_tokens.append((token, (line_index, part_index)))
                    except Exception:
                        self.lexical_errors.append("lexical error (" + str(line_index) + ", " + str(part_index) + ")")
                part_index += 1

            line_index += 1

        self.write_pif(all_tokens)
        self.write_st()
        return all_tokens

    def tokenize(self, line):
        for separator in self.separator_table.get_all():
            if separator != ' ':
                new_separator = ' ' + separator + ' '
                line = line.replace(separator, new_separator)

        for operator in self.operators_table.get_all():
            new_operator = ' ' + operator + ' '
            line = line.replace(operator, new_operator)

        tokens = line.split()

        composed_operators = ["==", "!=", "<=", ">="]
        index = 0
        while index < len(tokens) - 1:
            if (tokens[index] + tokens[index + 1]) in composed_operators:
                tokens[index] = tokens[index] + tokens[index + 1]
                tokens.pop(index + 1)
                index -= 1
            index += 1
        return tokens

    def is_operator(self, part):
        return self.operators_table.contains(part)

    def is_separator(self, part):
        return self.operators_table.contains(part)

    def is_keyword(self, part):
        return self.operators_table.contains(part)

    def valid_symbol(self, part):
        for char in part:
            if not self.characters_table.contains(char):
                raise Exception
        if part[0].isdigit():
            return False
        return True

    @staticmethod
    def write_pif(self, tokens):
        file = open("C://Users//Iasmina//PycharmProjects//FLCD//lab05//PIF.out", 'w')
        for token in tokens:
            file.write(str(token[0]) + "\t\t (" + str(token[1][0]) + ", " + str(token[1][1]) + ")\n")

    def write_st(self):
        file = open("C://Users//Iasmina//PycharmProjects//FLCD//lab05//ST.out", 'w')
        file.write(str(self.symbol_table))
