from week10.Grammar import Grammar
from week10.ParserOutput import ParserOutput

if __name__ == '__main__':
    grammar = Grammar("resources/g2.in")
    parserOutput2 = ParserOutput(grammar, "resources/output.txt")
    parserOutput2.runParsing()
