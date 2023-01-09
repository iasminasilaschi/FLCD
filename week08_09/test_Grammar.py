from week08_09.Grammar import Grammar


class TestGrammar:
    grammar = Grammar("resources/g1.in")

    def test_get_terminals(self):
        assert self.grammar.terminals == "a b c"

    def test_get_non_terminals(self):
        assert self.grammar.nonTerminals == "S A"

    def test_starting_symbol(self):
        assert self.grammar.startingSymbol == "S"

    def test_set_of_values(self):
        assert list(self.grammar.productionSet.getProductionSet().keys()) == ["S", "A"]
        assert self.grammar.productionSet.getProductionSet().get("S") == ["a", "A"]
        assert self.grammar.productionSet.getProductionSet().get("A") == ["b", "A", "c"]

    def test_if_CFG(self):
        assert self.grammar.productionSet.check_CFG()
