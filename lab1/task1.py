from sys import argv


def calculate(user_input): 
    if len(argv):
        try:
            return eval(''.join(argv[1:]))
        except:
            None

print(calculate(argv[1:]))