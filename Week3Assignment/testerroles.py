import numpy as np


class ManualTester:

    def analyze(self, data):
        print(f"First 5 Test execution times: {data[:5]}")

class AutomationTester:
    def analyze(self, data):
        print(f"Fastest Test execution time: {data.min()} seconds")
class PerformanceTester:

    def analyze(self, data):
        print(f"95th percentile Test execution time: {np.percentile(data, 95)} seconds")


def show_analysis(tester, data):
    tester.analyze(data)

if __name__ == "__main__":
    execution_times = np.array([30, 35, 50, 55, 70, 90, 40, 60, 80, 110, 120, 130])
    mt = ManualTester()
    show_analysis(mt, execution_times)

    at = AutomationTester()
    show_analysis(at, execution_times)

    pt = PerformanceTester()
    show_analysis(pt, execution_times)