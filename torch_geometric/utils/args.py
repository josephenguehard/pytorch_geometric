import inspect


def filter_args(func):
    """
    A decorator to filter inputs arguments of a function.

    Examples:
        >>> from torch_geometric.utils import filter_args
        >>> def f(x, y = None):
        ...     print("x: ", x, "y: ", y)
        >>> f(1, t = 3)
        >>> TypeError
        <BLANKLINE>
        >>> f = filter_args(f)
        >>> f(1, t = 3)
        >>> "x: 1, y: None"
    """
    def decorator(*args, **kwargs):
        # Get function arguments
        f_args = list(inspect.signature(func).parameters.keys())

        # Filter kwargs
        sub_kwargs = {k: kwargs[k] for k in f_args[len(args):] if k in kwargs}

        # Apply function
        return func(*args, **sub_kwargs)

    return decorator
