# I'm too lazy to actually calculate binary so I just made a program that does it for me :/

#Set some stuff initially so that errors dont ensue
def reset():
    global mode, decimal, binary, iteration
    mode = "c"
    decimal = "d"
    binary = "e"
    iteration = 0


def convertext():
    global decimal
    binarystr = ''
    while decimal.isdigit() == False:
        decimal = input("Type the decimal you want to convert to binary \n")
    while int(decimal) > 0:
        digit = int(decimal) % 2
        binarystr = (str(digit) + binarystr)
        decimal = int(decimal) // 2
    print(f"Your converted binary is {binarystr}")
    

def convertbinary():
    global binary, iteration
    equation = []
    while binary.isdigit() == False:
        binary = input("Type the binary you want to convert to decimal \n")
    blist = list((binary))
    blist.reverse() #reversing it so that we start from beginning to end, not end to beginning
    for bin in blist:
        equation.append(int(bin) * pow(2, iteration))
        iteration = iteration + 1
    print(f"Your converted number is {sum(equation)}")

def finish():
    exit =  input("Press enter to exit, or type 'c' if you want to convert another item \n")
    if exit == "c":
        reset()
        start()
    

def start():
    global mode
    while mode != "a" and mode != "b":
        mode = input(
        """Do you want to convert TO binary or convert FROM binary? \n 
        a. Convert decimal to binary \n 
        b. Convert binary to decimal \n""")

    if mode == "a":
        convertext()
    elif mode == "b":
        convertbinary()
    finish()

reset()
start()

    
