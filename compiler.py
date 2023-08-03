import utils

tempVars = 0
definedVars = {}
__tempVar_name__ = 'tmpVar'

def print_to_amongus(string=None, name=__tempVar_name__):
    lines = ''
    global tempVars
    tempVars += 1
    if(name == __tempVar_name__):
        for c in string:
            lines += 'GUYS I CAN VOUCH ' + __tempVar_name__ + str(tempVars) + ' IS ' + str(ord(c))
            lines += '\n' + __tempVar_name__ + str(tempVars) + ' CAN VOUCH GO AND TELL THEM COME ON\n'
        return lines
        
    return name + ' CAN VOUCH GO AND TELL THEM COME ON\n'


def comment(string, autoAllign=True):
    return string + "\n"

def string_to_amongus(string, name=__tempVar_name__):
    lines = ''
    i = 1
    if(len(string) == 1): #tempvar c
        return 'GUYS I CAN VOUCH ' + name + ' IS ' + str(ord(string)) + '\n'
    for c in string:
        if(name == __tempVar_name__):
            global tempVars 
            tempVars += 1
            i = tempVars
        lines += 'GUYS I CAN VOUCH ' + name + str(i) + ' IS ' + str(ord(c)) + '\n'
        i+=1
    return lines

def loop_to_amongus(n, string):
    lines = ''
    for i in range(n):
        lines += string + '\n'
    return lines
        

def define_var(name, value):
    if name in definedVars:
        return 'ERROR, the variable "' + name + '" has already been defined' + '\n'
    return 'GUYS I CAN VOUCH ' + name + ' IS ' + str(value) + '\n'
    
def redefine_var(name, value):
    return 'GUYS I CAN VOUCH ' + name + ' IS ' + str(value) + '\n'

def print_var(name):
    return name + ' CAN VOUCH GO AND TELL THEM COME ON\n'
    
def number_to_ascii(n, name):
    lines = ''
    lines += string_to_amongus(str(ord(str(n))), name) + '\n'
    return lines

def print_newline():
    return 'GUYS I CAN VOUCH string IS 10\nstring CAN VOUCH GO AND TELL THEM COME ON\n'

def substract_byte(name, n):
    return loop_to_amongus(n, name + ' GOES DOWN')
    
def exit_amongus():
    return 'GUYS I CAN VOUCH IS '
    
print(utils.importConstants())
print(comment("This is a comment."))
print(utils.exit_amongus_but_way_cooler())