import asyncio
import time
from icecream import ic


async def time_async_function(func, *args, **kwargs):
    """
    Times the execution of an asynchronous function and logs the result with icecream.
    Captures and returns the function's last return value.

    Parameters:
    - func: The asynchronous function to be timed.
    - *args: Arguments to pass to the function.
    - **kwargs: Keyword arguments to pass to the function. Includes 'number' for timeit repetitions if needed.

    Returns:
    - A tuple containing the execution time and the function's last return value.
    """
    number = kwargs.pop('number', 1)
    start_time = time.perf_counter()
    last_return_value = None

    for _ in range(number):
        last_return_value = await func(*args, **kwargs)

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    ic(execution_time)
    return execution_time, last_return_value


# Example usage for an asynchronous function
async def async_function(x):
    await asyncio.sleep(1)  # Simulate an async operation
    return x * 2


# Running and timing the async function
async def main():
    execution_time, result = await time_async_function(async_function, 10, number=1)
    ic(result)


asyncio.run(main())
