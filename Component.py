class Component:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Component({self.name})"

class Variable(Component):
    names = set()
    def __init__(self, name):
        self.name = name
        Variable.names.add(name)
    def __repr__(self):
        return f"Variable({self.name})"

class Quantifier(Component):
    def __init__(self, form, variable, containing_set):
        if form not in ["A", "E"]:
            raise ValueError("not a valid quantifier")
        self.form = form
        self.variable = variable
        self.set = CommonSet(containing_set)
    def __repr__(self):
        return f"Quantifier({self.form}, {self.variable}, {self.set})"

class CommonSet(Component):
    def __init__(self, name):
        if name not in ["N", "Z", "R", "Q", "C"]:
            raise ValueError("not a valid set")
        self.name = name
    def __repr__(self):
        return f"CommonSet({self.name})"

class Equation(Component):
    def __init__(self, form, left, right):
        if form not in ["=", "<", "<=", ">", ">="]:
            raise ValueError("not a valid equation")
        self.form = form
        self.left = left
        self.right = right
    def __repr__(self):
        return f"Equation({self.form}, {self.left}, {self.right})"