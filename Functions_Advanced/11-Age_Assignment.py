def age_assignment(*args, **kwargs):
    result = {}
    for arg in args:
        for kwarg in kwargs.keys():
            if arg[0] == kwarg:
                result[arg] = kwargs[kwarg]

    return result
