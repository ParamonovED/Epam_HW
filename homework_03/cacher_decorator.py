from collections.abc import Callable


def cache(times):
    def cacher(function: Callable) -> Callable:
        journal = {}

        def wrapper(*args, **kwargs):
            args_mod = tuple(str(i) for i in args)
            kwargs_mod = tuple(str(i) for i in kwargs.items())
            all_args = args_mod, kwargs_mod
            if journal.get(all_args) and journal.get(all_args)[1] > 0:
                result = journal.get(all_args)[0]
                journal[all_args][1] -= 1
            else:
                result = function(*args, **kwargs)
                journal[all_args] = [result, times]
            return result

        return wrapper

    return cacher
