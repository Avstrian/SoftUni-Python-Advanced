def func_executor(*args):
    result = []

    for func, func_args in args:
        result.append(func(*func_args))

    return result
