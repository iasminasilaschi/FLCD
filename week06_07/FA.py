class FA:
    def __init__(self, filename):
        self.Q_set_of_states = {}
        self.E_alphabet = {}
        self.q0_initial_state = {}
        self.F_set_of_final_states = {}
        self.T_transitions = {}
        self.read_input_file(filename)

    def read_input_file(self, filename):
        with open(filename) as f:
            self.Q_set_of_states = f.readline().strip().replace(" ", "")[3:-1].split(',')
            self.E_alphabet = f.readline().strip().replace(" ", "")[3:-1].split(',')
            self.q0_initial_state = f.readline().strip().replace(" ", "")[4:-1].strip(',')
            self.F_set_of_final_states = f.readline().strip().replace(" ", "")[3:-1].split(',')

            f.readline()
            self.T_transitions = {}

            for line in f:
                if line != '}' and len(line) > 0:
                    pair = line.strip().replace(" ", "").split('->')[0].strip()[1:-1].split(",")
                    origin = pair[0]
                    path = pair[1]
                    target = line.strip().replace(" ", "").split('->')[1].strip()

                    if (origin, path) in self.T_transitions.keys():
                        self.T_transitions[(origin, path)].append(target)
                    else:
                        self.T_transitions[(origin, path)] = [target]
            if not self.is_fa_valid():
                raise Exception("Error in input file!")

    def is_dfa(self):
        for key in self.T_transitions.keys():
            if len(self.T_transitions[key]) > 1:
                return False
        return True

    def is_accepted_by_fa(self, sequence):
        if self.is_dfa():
            start = self.q0_initial_state
            for c in sequence:
                if (start, c) in self.T_transitions.keys():
                    start = self.T_transitions[(start, c)][0]
                else:
                    return False
            if start in self.F_set_of_final_states:
                return True

        return False

    def check_if_null(self):
        if self.q0_initial_state in self.F_set_of_final_states:
            return True
        return False

    def is_fa_valid(self):
        if self.q0_initial_state not in self.Q_set_of_states:
            return False
        for final in self.F_set_of_final_states:
            if final not in self.Q_set_of_states:
                return False
        for (origin, path) in self.T_transitions.keys():
            if origin not in self.Q_set_of_states:
                return False
            if path not in self.E_alphabet:
                return False
            for target in self.T_transitions[(origin, path)]:
                if target not in self.Q_set_of_states:
                    return False
        return True

    def __str__(self):
        T = ""
        for (origin, path) in self.T_transitions.keys():
            T += "(" + str(origin) + "," + str(path) + ")" + "->" + str(self.T_transitions[(origin, path)]) + "\n"
        return "Q_set_of_states = " + str(self.Q_set_of_states) + "\n" + "E_alphabet = " + str(
            self.E_alphabet) + "\n" + "q0_initial_state = {" + str(
            self.q0_initial_state) + "}\n" + "F_set_of_final_states = " + str(
            self.F_set_of_final_states) + "\n" + "T_transitions = {\n" + T + "\n"
