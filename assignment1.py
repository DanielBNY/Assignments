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


