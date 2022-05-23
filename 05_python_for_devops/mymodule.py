<<<<<<< HEAD
#!/usr/bin python3

def calculate(op_a, op_b,operator):
    if operator == '+':
        return op_a + op_b
    if operator == '-':
        return op_a - op_b
    if operator == '*':
        return op_a * op_b
    if operator == '/':
        try:
            return op_a / op_b
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            return None
        if operator == "log":
            try:
                return math.log(op_a) / math.log(op_b)
            except ValuseError:
                print('Cannot take log of 0!")
                return None
            except ZeroDivisionError:
                print("Cannot take log base 1!")
                return None
            else:
                return result
=======
# This is a module
# It lives in the file mymodule.py

def dummy():
    return 45

def foo():
    print('bar!')
    return 1

public_data = "public stuff!"
# names that begin with _ are considered "private"
_private_data = "private stuff!"
>>>>>>> 584a75b437188de8bab001c0b2aa7a529a044c24
