from lab05.Scanner import Scanner

if __name__ == '__main__':
    scanner = Scanner()

    p1 = "C://Users//Iasmina//PycharmProjects//FLCD//lab05//p1.txt"
    p2 = "C://Users//Iasmina//PycharmProjects//FLCD//lab05//p2.txt"
    p3 = "C://Users//Iasmina//PycharmProjects//FLCD//lab05//p3.txt"
    p1_err = "C://Users//Iasmina//PycharmProjects//FLCD//lab05//p1-err.txt"

    try:
        print(scanner.scan(p1))
        print(scanner.lexical_errors)
    except Exception as exception:
        print(exception)
