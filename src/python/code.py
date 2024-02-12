from timeit import Timer
from icecream import ic


def time_function(func, *args, **kwargs):
    """
    Times the execution of a function using timeit and logs the result with icecream.

    Parameters:
    - func: The function to be timed.
    - *args: Arguments to pass to the function.
    - **kwargs: Keyword arguments to pass to the function. Includes 'number' for timeit repetitions if needed.

    Returns:
    - The execution time of the function.
    """
    # Extract the 'number' keyword argument for timeit, defaulting to 1 if not provided
    number = kwargs.pop('number', 1)

    # Setup the timer with the provided function and arguments
    t = Timer(lambda: func(*args, **kwargs))

    # Time the function execution
    execution_time = t.timeit(number=number)

    # Log the execution time
    ic(execution_time)

    return execution_time


# Example usage
def my_function(x):
    """Example function that generates a string from 0 to x-1."""
    return "-".join(str(n) for n in range(x))


# Timing 'my_function' with argument 100
time_function(my_function, 100)
