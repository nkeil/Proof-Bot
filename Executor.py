from Component import *
from Algebra import find_solution

def execute(prop, method):
    quantifiers = get_quantifiers(prop)
    if len(quantifiers) == 1 and quantifiers[0].form == 'E':
        print("Existence proof")
        

    if method == "d":
        print("We proceed directly")
        print(prop)

        

def get_quantifiers(prop):
    quantifiers = []
    for c in prop:
        if isinstance(c, Quantifier):
            quantifiers.append(c)
        else:
            break
    return quantifiers