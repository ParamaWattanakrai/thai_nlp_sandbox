A = True
B = False

def do():
    print('Passed!')

def check():
    if A == True:
        if B == False:
            do()
        else:
            print('B is False')
    else:
        print('A is True')

def better_check():
    if A != True:
        return print('A is False')
    if B != False:
        return print('B is True')
    do()

better_check()