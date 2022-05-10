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
