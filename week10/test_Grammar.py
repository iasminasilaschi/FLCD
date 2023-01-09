from week11.Grammar import Grammar


class TestGrammar:
    grammar2 = Grammar("resources/g2.in")

    def test_get_terminals(self):
        assert self.grammar2.terminals == "\"BEGIN\" \";\" \"END\" \"BOOL\" \"CHAR\" \"INT\" \"FLOAT\" \"ARRAY\" \"[" \
                                          "\" \"]\" \"OF\" \"TYPEDEF\" \"{\" \"}\" \"=\" \"+\" \"*\" \"(\" \")\" " \
                                          "\"READ\" \"WRITE\" \"IF\" \"ELSE\" \"THEN\" \"WHILE\" \"<\" \"<=\" \"==\" " \
                                          "\"!=\" \">=\" \">\""

    def test_get_non_terminals(self):
        assert self.grammar2.non_terminals == "program decllist declaration type1 arraydecl type userdef cmpdstmt " \
                                              "stmtlist stmt simplstmt assignstmt expression term factor iostmt " \
                                              "structstmt ifstmt whilestmt condition relation"

    def test_starting_symbol(self):
        assert self.grammar2.starting_symbol == "term"

    def test_if_CFG(self):
        assert self.grammar2.production_set.getIsCFG()
