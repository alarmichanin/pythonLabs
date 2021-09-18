user_input = input("Enter your expression: ")
main_str = ''

def checkEBNF(use_input):
    '''
    checkEBNF - it's a function for cheking :
    1) Is the current element a number if not , check is it + or -
    2) Check if after + or - we have number
    3) In other variant we get phrase "(False,None)".
    '''
    global main_str
    if len(use_input):
        if use_input[0].isdigit():
            main_str+=use_input[0]
            return checkEBNF(use_input[1:])
        elif use_input[0] in '+-':
            try:
                if use_input[1].isdigit():
                    main_str+=use_input[0]+use_input[1]
                    return checkEBNF(use_input[2:])
                else:
                    return (False,None)
            except IndexError:
                return (False,None)
        else:
           return (False,None)
    else:
        return (True,eval(main_str))
if len(user_input):
    if user_input[0].isdigit():
        main_str+=user_input[0]
        print(checkEBNF(user_input[1:]))
    else:
        print("(False,None)")
else:
    print("(False,None)")
