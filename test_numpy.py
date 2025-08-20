import numpy as np
import timeit

N = 1_000_000
rep = 100

py_list = list(range(N))
np_array = np.arange(N)

def py_square():
    # return [x**2 for x in py_list]
    xsq = []
    for x in py_list:
        xsq.append(x**2)
    return xsq

def np_square():
    return np_array**2

py_time = timeit.timeit(py_square, number=rep)
np_time = timeit.timeit(np_square, number=rep)

print("Pythonic way : total={:.3f}s avg={:.3f}ms/call".format(py_time, py_time/rep*1e3))
print("Numpy way    : total={:.3f}s avg={:.3f}ms/call".format(np_time, np_time/rep*1e3))

"""
Pythonic way : total=5.856s avg=58.555ms/call
Numpy way    : total=0.137s avg=1.370ms/call
"""
