from collections.abc import Callable


def cache(function: Callable, times) -> Callable:
    journal = {}

    def wrapper(*args):
        if journal.get(args):
            if journal.get(args)[1] > 0:
                result = journal.get(args)[0]
                journal[args][1] -= 1
            else:
                journal.pop(args)
                result = function(*args)
                journal[args] = [result, times]
        else:
            result = function(*args)
            journal[args] = [result, times]
        return result

    return wrapper
