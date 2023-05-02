
#target: to calculate the speed using the formula: V=D/T
#        the user will provide the formula with the desired parameters

def find_operator(p_value):
    operators = "+-*/"
    for i in range(4):
        if p_value.find(operators[i]) > 0:
            operator = p_value.find(operators[i])
            break
    #return p_value[operator]
    return operator, p_value[operator]

#---------------------------------------------
def ret_type(pvalor):
    try:
        float(pvalor)
        return "num"
    except:
        return "str"

#----------------------------------------
def validate_parts(pPart1, pPart2, pPart3):
    v_count = 0

    if ret_type(pPart1) == "num": v_count = v_count+1
    if ret_type(pPart2) == "num": v_count = v_count+1
    if ret_type(pPart3) == "num": v_count = v_count+1
  
    if v_count == 2:
        return "OK"
    else:
        return "missing value(s)"

#--------------------------------
def calculation(pFormula):
    #return: 
    #   <vale>: solution of the equation
    #     -900: incorrect formula
    #     -901: missing values

    #step1: find the equals sign and divide the equation into 2 parts
    parts = pFormula.split("=")
    part1 = parts[0].strip()
    aux = parts[1].strip()

    #step2: to find the operador (+, -, /, *) 
    operator = find_operator(aux)    
    if operator[0] == -1:
        return "missing operator"
    
    #operator found
    aux = aux.split(operator[1])
    part2 = aux[0]
    part3 = aux[1]
    
    #check if formula is correct
    ret = validate_parts(part1, part2, part3)
    if ret != "OK":
        return ret

    #return the result of the equation
    if ret_type(part1) == "str":
        #formula = "V = <num> <operator> <num>"
        part2 = float(part2)
        part3 = float(part3)
        
        if operator[1] == "+": calc = part2 + part3
        elif operator[1] == "-": calc = part2 - part3
        elif operator[1] == "*": calc = part2 * part3
        elif operator[1] == "/": calc = part2 / part3
        print("calc:", calc)
    elif ret_type(part2) == "str":
        part1 = float(part1)
        part3 = float(part3)
        
        if operator[1] == "+": calc = part1 - part3
        elif operator[1] == "-": calc = part1 + part3
        elif operator[1] == "*": calc = part1 / part3
        elif operator[1] == "/": calc = part1 * part3

    elif ret_type(part3) == "str":
        part1 = float(part1)
        part2 = float(part2)
        
        if operator[1] == "+": calc = part1 - part2
        elif operator[1] == "-": calc = part1 + part2
        elif operator[1] == "*": calc = part1 / part2
        elif operator[1] == "/": calc = part1 * part2

    return calc
#-----------------------------------------------------------------
# some tests
#-----------------------------------------------------------------
def meus_testes():
    test = "V = 100/2"

    #print(">> with method find():")
    #part1 = test[0:test.find("=")].strip()
    #aux = test[test.find("=")+1:].strip()
    #print("part1: ", part1, "type str?", isinstance(part1, str))
    #print("part1: ", aux, "\n")

    #print(">> with method split():")
    parts = test.split("=")
    part1 = parts[0].strip()
    aux = parts[1].strip()
    print("parts: ", parts)
    print("part1: ", part1)
    print("aux: ", aux)

    print(">> call function find_operator():")
    operator1 = find_operator(aux)
    print("operator1:", operator1)

    #checks if it found the operator
    if operator1[0] > -1:
        #operator found
        aux = aux.split(operator1[1])
        print("aux:", aux)
        part2 = aux[0]
        part3 = aux[1]

        print("part1: ", part1, " => part2: ", part2, " => operator: ", operator1[1], " => part3: ", part3)
        print("formula =>  ", part1 + " = " + part2 + " " + operator1[1] + " " + part3)

        print("validate:", validate_parts(part1, part2, part3))

    print(">>> chamada da funtion calculatio(): ", calculation(test))

#chama função de testes
#meus_testes

#principal
#  the user will provide the formula with the desired parameters
print("<<  ( V = D/T ) This formula allows you to calculate, speed, distance or time >>\n")
vFormula = input("Enter the velocity formula providing the desired parameters: ")
print(">> The result of the formula is: ", calculation(vFormula))
