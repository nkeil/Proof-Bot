import Component

def parse(s):
    s = clean(s)
    parts = []
    while len(s) > 0:
        s, part = parse_next(s, parts)
        parts.append(part)
    return parts

def parse_next(s, parts):
    if s[0] == "(":
        return parse_tail(s[1:], parts)
    elif s[0] in ["A", "E"]:
        return parse_quantifier(s)
    elif s[0].isdigit():
        return parse_numeral(s)
    elif s[0] in ["=", "<", ">"]:
        return parse_equation(s, parts)
    elif s[0] in Component.Variable.names:
        return parse_variable(s)
    else:
        raise SyntaxError("Invalid Expression")

def parse_tail(s, parts):
    parts = []
    while len(s) != 0 and s[0] != ")":
        s, part = parse_next(s, parts)
        parts.append(part)
    if len(s) == 0:
        raise SyntaxError("No closing parenthesis")
    return s[1:]

def parse_quantifier(s):
    if len(s) < 5:
        raise SyntaxError("Invalid quantifier")
    if s[1] in Component.Variable.names:
        raise SyntaxError(f"Quantifier: name already exists ({s[1]})")
    var = Component.Variable(s[1])
    return s[5:], Component.Quantifier(s[0], var, s[4])

def parse_numeral(s):
    number = ""
    while len(s) > 0 and (s[0].isdigit() or s[0] == '.'):
        number += s[0]
        s = s[1:]
    number = (float if '.' in number else int)(number)
    return s, number

def parse_equation(s, parts):
    rel, s = s[0], s[1:]
    if len(s) > 1 and s[0] == "=":
        rel += s[1]
        s = s[1:]
    if len(s) == 0 or len(parts) == 0:
        raise SyntaxError("Invalid equation")
    left = parts.pop()
    s, right = parse_next(s, parts)
    return s, Component.Equation(rel, left, right)
    
def parse_variable(s):
    return s[1:], Component.Variable(s[0])

def clean(s):
    return ''.join(c for c in s if c not in [' ', ','])