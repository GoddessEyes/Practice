def quote(prefix, postfix):
    def real_decorator(function):
        def wrapper(string):
            return prefix + function(string) + postfix
        return wrapper
    return real_decorator


#@quote('<', '>')
def print_str(string):
    return string


print(print_str('I love Python!'))
