from lab04.Scanner import Scanner

if __name__ == '__main__':
    scanner = Scanner()

    p1 = "C://Users//Iasmina//PycharmProjects//FLCD//lab01//p1.txt"
    p2 = "C://Users//Iasmina//PycharmProjects//FLCD//lab01//p2.txt"
    p3 = "C://Users//Iasmina//PycharmProjects//FLCD//lab01//p3.txt"
    p1_err = "C://Users//Iasmina//PycharmProjects//FLCD//lab01//p1-err.txt"

    scanner.scan(p1)
    if scanner.lexical_errors:
        for error in scanner.lexical_errors:
            print(error)
    else:
        print("lexically correct")
