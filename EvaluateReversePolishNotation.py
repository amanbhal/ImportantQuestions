"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

def evalRPN(tokens):
    stack = []
    for i in range(len(tokens)):
        #if ord(tokens[i])>=48 and ord(tokens[i])<=57:
        if (tokens[i].isdigit()) or (tokens[i].startswith('-') and tokens[i][1:].isdigit()):
            stack.append(int(tokens[i]))
        else:
            a = stack.pop()
            b = stack.pop()
            if tokens[i]=="+":

                stack.append(a+b)
            elif tokens[i]=="-":
                stack.append(b-a)
            elif tokens[i]=="*":
                stack.append(a*b)
            else:
                if float(float(b)/float(a))<0:
                    stack.append(int(math.ceil(float(float(b)/float(a)))))
                else:
                    stack.append(b/a)
    return stack.pop()

print evalRPN(["2", "1", "+", "3", "*"])