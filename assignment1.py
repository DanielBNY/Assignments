import random


def reverse_func(input_func):
    """
    function decorator that reverses the target function’s positional
    arguments (however has no effect on keyword arguments).
    :param input_func: input function
    :return: function with reversed input (only with args parameters)
    """
    def manipulated_reverse_func(*args, **kwargs):
        if args:
            result = input_func(*args[::-1])
            return result
        if kwargs:
            result = input_func(**kwargs)
            return result

    return manipulated_reverse_func


@reverse_func
def sub(a, b):
    return a - b


LEGAL_LETTERS = ["A", "B", "C"]


def math_formula(input_formula: str, num_outputs: int):
    """
    The function receives as an input a string input_formula and num_outputs number.
    The string input_formula includes a valid mathematical formula on variables named
    A,B and C (example: s=’2*A+B/C’). The function selects n times random positive
    integers A,B and C (in range 1-100) and prints the formula and its results.
    :param input_formula: str
    :param num_outputs: int
    :return: None
    """
    original_input_formula = input_formula
    for i in range(1, num_outputs):
        input_formula = original_input_formula
        for char in input_formula:
            if char.isalpha():
                if char in LEGAL_LETTERS:
                    random_number = random.randint(1, 100)
                    input_formula = input_formula.replace(char, str(random_number))
                else:
                    raise Exception("A non legal parameter input was given.\nThe legal parameters are: "+str(LEGAL_LETTERS))
        print(str(input_formula), '=', eval(input_formula))
