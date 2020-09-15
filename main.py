import Parser, Executor

def get_proposition():
    while True:
        try:
            prop = Parser.parse(input("Enter proposition: "))
            return prop
        except SyntaxError as e:
            print("Syntax:", e)
        except ValueError as e:
            print("Value:", e)

def get_method():
    method = ""
    while method not in ["d", "cp", "cd", "i"]:
        method = input("Enter method (d, cp, cd, i): ")
    return method

def main():
    prop = get_proposition()
    method = get_method()
    Executor.execute(prop, method)

if __name__ == "__main__":
    main()
