#Calculator (Dum Down Version)
import math

def mainmenu():
    print("  ____      _            _       _             _ \n / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __| | \n | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__| | \n | |__| (_| | | (__| |_| | | (_| | || (_) | |  |_| \n \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|  (_) \n ")
    
    choice = input('\n1. Caculator\n2. Instructions\n3. Mathematical Functions\n4. Formulas\n5. Formulas List\n6. Quit\n\nChoice: ')
    
    if choice == "1":
        calculator()
    elif choice == "2":
        instructions()
    elif choice == "3":
        functions()
    elif choice == "4":
        formula()
    elif choice == "5":
        formlist()
    elif choice == "6":
        quit()
    else:
        print('Not A Valid Answer Try Again')

def formlist():
    print("\n\nQuadratic Formula: 1\nAverage Formula: 2\n\n")
    input('Enter To Return To Main Menu')
    mainmenu()
def formula():
    fc = input("Formula Number: ")
    if fc == "1":
        try:
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
        except ValueError:
            print("Incorrect Input.")
            mainmenu()
        var1 = b*-1
        var2 = b*b
        var2 = abs(var2)
        var3 = 4*a*c
        var4 = 2*a
        var2 = var2-var3
        if 0 > var2:
            print("√", var2)
            print("NRR Error")
            mainmenu()
        var2 = var2 ** 0.5
        fr = var1-var2
        fr = fr/var4
        sr = var1+var2
        sr = sr/var4
        print(fr, u"\u00B1" , sr)
        mainmenu()
    elif fc == "2":
        aod = int(input("aod: "))
        store = []
        for i in range(0, aod):
            n = float(input("num: "))
            store.append(n)
        ammount = sum(store)
        ammount /= aod
        print("average: " + ammount)
        mainmenu()
def calculator():
    fs = ["!", "^", "√"]
    try:
        bn = float(input('n: '))
    except ValueError:
        print('Thats Not A Valid Number')

        
    while True:
        ars = input('a: ')

        if ars == '=':
            print(bn)
            mainmenu()
        elif ars == "f" or ars == "F":
            cf = input('f: ')
            if cf == "!" or cf == "FACT" or cf == "fact" or cf == "1":
                bn = math.gamma(bn+1)
            elif cf == "^" or cf  == "POW" or cf == "pow" or cf == "2":
                hm = float(input('n: '))
                bn = bn**hm
            elif cf == "√" or cf == "SQRT" or cf == "sqrt" or cf == "3":
                bn = bn**0.5
            elif cf == ";" or cf == "NOP" or cf == "nop" or cf == "4":
                continue
            elif cf == ">" or cf == "CEIL" or cf == "5":
                bn = math.ceil(bn)
            elif cf == "<" or cf == "FLOOR" or cf == "6":
                bn = math.floor(bn)
            elif cf not in fs:
                print('INVALID FUNCTION')
                mainmenu()
                
        elif ars == "q":
            mainmenu()
            
        if ars != "f":
            try:
                nn = input('n: ')
            except ValueError:
                print('Thats Not A Valid Number')
                mainmenu()
            if ars == "+" or ars == "add":
                nn = float(nn)
                bn += nn
            elif ars == "-" or ars == "subtract":
                nn = float(nn)
                bn -= nn
            elif ars == "*" or ars == "x" or ars == "×" or ars == "multiply":
                nn = float(nn)
                bn *= nn
            elif ars == "/" or ars == "÷" or ars == "divide":
                nn = float(nn)
                if nn == 0:
                    print('Zero Cannot Be Dividing')
                    break
                bn /= nn
            elif nn == '=':
                print(bn)
                mainmenu()
            else:
                continue
        
def instructions():
    print("\nHow this program works is when you start the calculator(press 1), it will say 'n' which means \nnumber and then after you enter your number you will see a 'a' which stands for arithmetic operations which means \nadd(+), subtract(-), multiply(* or x), divide(/). Now to get the result of ur equation what you do is use the = sign \nand then the program will output the result of the equation. Now to access functions what you do is when the 'a' comes \nup put in'f' and that will alter mode into function mode (to review what functions are avaliable press 3 when in menu.) \nand to get the answer press the = sign. ")
    input('\nEnter To Return To Main Menu')
    mainmenu()

def functions():
    print("\n! or FACT = Factorial\n^ or POW = Exponents \n√ or SQRT = Square Root\n; or NOP = No Operation\n> or CEIL = Round Number Up\n< or FLOOR = Round Number Down\n\n")
    input('Enter To Return To Main Menu')
    mainmenu()
mainmenu()



