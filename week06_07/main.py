from FA import FA
from week06_07.Scanner import Scanner

if __name__ == '__main__':

    fa = FA("resources/FA.in")
    print("Welcome!")

    while True:
        print("\n1. Scanner")
        print("2. FA")
        print("3. Exit")

        option = input("\nOption: ")

        if option == "1":

            scanner = Scanner()

            p1 = "resources/p1.txt"
            p2 = "resources/p2.txt"
            p3 = "resources/p3.txt"
            p1_err = "resources/p1-err.txt"

            while True:
                print("\n1. Program p1")
                print("2. Program p2")
                print("3. Program p3")
                print("4. Program p1_err")
                print("5. Back to main menu")

                option = input("\nOption: ")

                if option == "1":
                    scanner.scan(p1)
                elif option == "2":
                    scanner.scan(p2)
                elif option == "3":
                    scanner.scan(p3)
                elif option == "4":
                    scanner.scan(p1_err)
                elif option == "5":
                    break
                else:
                    print("Invalid option!")

                if scanner.lexical_errors:
                    for error in scanner.lexical_errors:
                        print(error)
                else:
                    print("lexically correct")

        elif option == "2":

            while True:
                print("\n1. See the set of states")
                print("2. See the alphabet")
                print("3. See the transitions")
                print("4. See the initial states")
                print("5. See the set of final states")
                print("6. Check if DFA")
                print("7. Check if it is accepted")
                print("8. Back to main menu")

                option = input("\nOption: ")

                if option == "1":
                    print('Q = {' + ', '.join([str(x) for x in fa.Q_set_of_states]) + '}')

                elif option == "2":
                    print('E = {' + ', '.join([str(x) for x in fa.E_alphabet]) + '}')

                elif option == "3":
                    T = ""
                    for (origin, path) in fa.T_transitions.keys():
                        T += "(" + str(origin) + "," + str(path) + ")" + "->" + str(
                            fa.T_transitions[(origin, path)]) + "\n"
                    print('T = {\n' + T + '}')

                elif option == "4":
                    print("q0 = {" + str(fa.q0_initial_state) + "}")

                elif option == "5":
                    print('F = {' + ', '.join([str(x) for x in fa.F_set_of_final_states]) + '}')

                elif option == "6":
                    print(fa.is_dfa())

                elif option == "7":
                    if fa.is_dfa():
                        sequence = input("Input sequence: ")
                        split_sequence = sequence.split(",")
                        if len(split_sequence) == 1:
                            print(fa.check_if_null())
                        else:
                            print(fa.is_accepted_by_fa(split_sequence))
                    else:
                        print("It is not DFA!")

                elif option == "8":
                    break
                else:
                    print("Invalid option!")

        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")
