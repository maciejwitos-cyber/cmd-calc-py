import sys

def usage():
    print(f"Usage: {sys.argv[0]} number1 operation number2")
    print("Available operations:")
    print("\tadd")
    print("\tsub")
    print("\tmul")
    print("\tdiv\n")


def main():

    if (len(sys.argv) == 4):

        # sys.argv[0] - nazwa programu
        # sys.argv[1] - pierwsza liczba
        # sys.argv[2] - działanie
        # sys.argv[3] - druga liczba

        num1 = int(sys.argv[1])
        num2 = int(sys.argv[3])

        match sys.argv[2]:

            case "add":
                print(f"{num1} +{num2} = {num1 + num2}")
            case "sub":
                print(f"{num1} - {num2} = {num1 - num2}")
            case "mul":
                print(f"{num1} * {num2} = {num1 * num2}")
            case "div":
                print(f"{num1} / {num2} = {num1 / num2}")
            case _:
                usage()

    else:
        usage()

if __name__ == '__main__':
    main()

