import sys
import time


class Benchmark:
    def __init__(self, interval: int, n1: int = 6, n2: int = 24):
        self.interval = interval
        self.n1 = n1
        self.n2 = n2

    def add(self) -> float:
        start = time.time()
        for _ in range(self.interval):
            (self.n1 + self.n2)
        end = time.time()
        return end - start

    def subtract(self) -> float:
        start = time.time()
        for _ in range(self.interval):
            (self.n1 - self.n2)
        end = time.time()
        return end - start

    def multiply(self) -> float:
        start = time.time()
        for _ in range(self.interval):
            (self.n1 * self.n2)
        end = time.time()
        return end - start

    def divide(self) -> float:
        start = time.time()
        for _ in range(self.interval):
            (self.n1 / self.n2)
        end = time.time()
        return end - start

    def power(self) -> float:
        start = time.time()
        for _ in range(self.interval):
            (self.n1 ** self.n2)
        end = time.time()
        return end - start

    def root(self) -> float:
        start = time.time()
        for _ in range(self.interval):
            (self.n1 ** (1/self.n2))
        end = time.time()
        return end - start


def main(interval: int):
    bench = Benchmark(interval)

    add: float = bench.add()
    subtract: float = bench.subtract()
    multiply: float = bench.multiply()
    divide: float = bench.divide()
    power: float = bench.power()
    root: float = bench.root()

    print(f"Addition took         {add:.3f} seconds.")
    print(f"Subtraction took      {subtract:.3f} seconds.")
    print(f"Multiplication took   {multiply:.3f} seconds.")
    print(f"Division took         {divide:.3f} seconds.")
    print(f"Exponents took        {power:.3f} seconds.")
    print(f"Roots took            {root:.3f} seconds.")

if __name__ == "__main__":
    times: int
    try:
        times = int(sys.argv[1])
    except IndexError:
        print("Give me a number of times to complete the operations.")
        sys.exit(1)

    main(times)
