import numpy as np


class TestReport:

    def __init__(self, nparray):
        self.nparray = nparray

    def average_time(self):
        print(f"Mean Execution Time: {self.nparray.mean()}")

    def max_time(self):
        print(f"Max Execution Time: {self.nparray.max()}")


class RegressionReport(TestReport):

    def __int__(self, nparray):
        super().__init__(nparray)

    def slow_tests(self, threshold):
        print(f"Test with slow execution time: {self.nparray[self.nparray > threshold]}")


if __name__ == "__main__":
    np_array = np.array([30, 50, 70, 90, 40, 60, 80, 110, 120, 130])
    execution_time_limit = 120
    rr1 = RegressionReport(np_array)
    rr1.average_time()
    rr1.max_time()
    rr1.slow_tests(execution_time_limit)
