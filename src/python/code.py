from timeit import Timer
from icecream import ic


def time_function_and_return_value(func, *args, **kwargs):
    """
    Times the execution of a function using timeit, logs the result with icecream,
    and returns the function's execution time and its return value.

    Parameters:
    - func: The function to be timed.
    - *args: Arguments to pass to the function.
    - **kwargs: Keyword arguments to pass to the function. Includes 'number' for timeit repetitions if needed.

    Returns:
    - A tuple containing the execution time and the function's return value.
    """
    # Extract the 'number' keyword argument for timeit, defaulting to 1 if not provided
    number = kwargs.pop('number', 1)

    # Capture the function's return value by executing it once
    # This execution is not timed to avoid affecting the return value with multiple executions
    return_value = func(*args, **kwargs)

    # Setup the timer with the provided function and arguments
    t = Timer(lambda: func(*args, **kwargs))

    # Time the function execution
    execution_time = t.timeit(number=number)

    # Log the execution time
    ic(execution_time)

    # Return both the execution time and the function's return value
    return execution_time, return_value


# Example usage
def my_function(x):
    """Example function that generates a string from 0 to x-1."""
    return "-".join(str(n) for n in range(x))


# Timing 'my_function' with argument 100 and capturing its return value
execution_time, result = time_function_and_return_value(my_function, 100)
ic(result)
