from timeit import Timer


def my_function():
    return "-".join(str(n) for n in range(100))


t = Timer(lambda: my_function())
print(t.timeit(number=10000))
