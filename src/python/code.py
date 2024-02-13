import asyncio
from timeit import Timer
from icecream import ic


def time_function(func, *args, is_async=False, **kwargs):
    """
    Times the execution of a function (sync or async) and logs the result with icecream.
    Captures and returns the function's last return value.

    Parameters:
    - func: The function to be timed.
    - *args: Arguments to pass to the function.
    - is_async: Specifies if the function is asynchronous.
    - **kwargs: Keyword arguments to pass to the function. Includes 'number' for timeit repetitions if needed.

    Returns:
    - A tuple containing the execution time and the function's last return value.
    """
    number = kwargs.pop('number', 1)
    last_return_value = None

    if is_async:
        async def wrapper():
            return await func(*args, **kwargs)

        async def time_async():
            nonlocal last_return_value
            start_time = asyncio.get_event_loop().time()
            for _ in range(number):
                last_return_value = await wrapper()
            end_time = asyncio.get_event_loop().time()
            return end_time - start_time

        execution_time = asyncio.run(time_async())
    else:
        def wrapper():
            return func(*args, **kwargs)

        t = Timer(lambda: wrapper())
        execution_time = t.timeit(number=number)
        last_return_value = wrapper()  # Get the last return value after timing

    ic(execution_time)
    return execution_time, last_return_value


# Example usage for a synchronous function
def sync_function(x):
    return x * 2


execution_time, result = time_function(sync_function, 10)
ic(result)


# Example usage for an asynchronous function
async def async_function(x):
    return x * 2


execution_time, result = time_function(async_function, 10, is_async=True)
ic(result)
