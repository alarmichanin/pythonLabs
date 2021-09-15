input = input("Enter your expression: ")
str = ''

def checkEBNF(input,str):
    '''
    checkEBNF - it's a function for cheking :
    1) Is the current element a number if not , check is it + or -
    2) Check if after + or - we have number
    3) In other variant we get phrase "(False,None)".
    '''
    if(len(input) != 0):
        if(input[0].isdigit()):
            str+=input[0]
            checkEBNF(input[1:],str)
        elif(input[0] == '+' or input[0] == '-'):
            if(input[1].isdigit()):
                str+=input[0]+input[1]
                checkEBNF(input[2:],str)
            else:
                print("(False,None)")
        else:
            print("(False,None)")
    else:
        return print("(True, ",eval(str),")")
if(len(input) != 0):
    if(input[0].isdigit()):
        checkEBNF(input[1:],str)
    else:
        print("(False,None)")
else:
    print("(False,None)")
