import copy
from Component import Equation, Variable
# These functions deal with solving SINGLE variable equations

def find_solution(eq):
    """ returns the solutions for the given single variable Equation
    [...]: list of solution(s)
    True: equation is a tautology

    >>> find_solution(Equation('=', Variable("x"), 2))
    2
    >>> find_solution(Equation('<', Variable("x"), 2))
    float('inf')
    """
    eq = isolate_variable(eq)
    if eq.form == '=':
        if not isinstance(eq.left, Variable) and not isinstance(eq.right, Variable):
            return eq.left == eq.right
        return [eq.left] if isinstance(eq.right, Variable) else [eq.right]



def isolate_variable(eq):
    """ returns a new equation that is equivalent to the given equation
        but has isolated the variable to at most one side

    >>> isolate_variable(Equation("=", Variable("x"), Variable("x")))
    Equation("=", 1, 1)
    >>> Equation("=", Variable("x"), 2)
    Equation("=", Variable("x"), 2)
    """
    eq = copy.deepcopy(eq)
    if isinstance(eq.left, Variable) or isinstance(eq.left, Variable):
        return eq

    return eq