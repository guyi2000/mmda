import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
import matplotlib.pyplot as plt
import scienceplots  # noqa
from threadpoolctl import threadpool_limits

from utils import time_mon, mem_mon, auto_mon_with_n  # noqa


def generate_K_1(n: int) -> np.ndarray:
    return (
        2 * sp.eye(n) - sp.diags(np.ones(n - 1), 1) - sp.diags(np.ones(n - 1), -1)
    ).tocsc()


def generate_K_2(n: int) -> np.ndarray:
    return 2 * np.eye(n) - np.diag(np.ones(n - 1), 1) - np.diag(np.ones(n - 1), -1)


def generate_K_3(n: int) -> np.ndarray:
    if n == 1:
        return np.array([[2]])
    row = np.zeros(n)
    row[0] = 2
    row[1] = -1
    return la.toeplitz(row)


def solve_n(n: int) -> tuple:

    @time_mon
    def solve_with_solve_1():
        K = generate_K_2(n)
        f = np.zeros(n)
        f[0] = 1
        np.linalg.solve(K, f)

    @mem_mon
    def solve_with_solve_2():
        K = generate_K_2(n)
        f = np.zeros(n)
        f[0] = 1
        np.linalg.solve(K, f)

    @time_mon
    def solve_with_inv_1():
        K = generate_K_2(n)
        f = np.zeros(n)
        f[0] = 1
        np.linalg.inv(K) @ f

    @mem_mon
    def solve_with_inv_2():
        K = generate_K_2(n)
        f = np.zeros(n)
        f[0] = 1
        np.linalg.inv(K) @ f

    time1 = solve_with_solve_1()
    mem1 = solve_with_solve_2()
    time2 = solve_with_inv_1()
    mem2 = solve_with_inv_2()

    @time_mon
    def solve_with_sparse_1():
        K = generate_K_1(n)
        f = np.zeros(n)
        f[0] = 1
        sp.linalg.spsolve(K, f)

    @mem_mon
    def solve_with_sparse_2():
        K = generate_K_1(n)
        f = np.zeros(n)
        f[0] = 1
        sp.linalg.spsolve(K, f)

    time3 = solve_with_sparse_1()
    mem3 = solve_with_sparse_2()
    return time1, time2, time3, mem1, mem2, mem3


def plot():
    n_tests = [1, 3, 10, 30, 100, 300, 1000, 3000, 10000]
    times1, times2, times3 = [], [], []
    mems1, mems2, mems3 = [], [], []
    with threadpool_limits(limits=1, user_api="blas"):
        for n_test in n_tests:
            sol = solve_n(n_test)
            times1.append(sol[0])
            times2.append(sol[1])
            times3.append(sol[2])
            mems1.append(sol[3])
            mems2.append(sol[4])
            mems3.append(sol[5])

    plt.style.use(["science", "ieee", "grid"])
    plt.subplots(2, 1, figsize=(6, 6), dpi=300)

    plt.subplot(2, 1, 1)

    plt.plot(n_tests, times1, label="solve")
    plt.plot(n_tests, times2, label="inv")
    plt.plot(n_tests, times3, label="sparse")

    plt.title("Time Consumption", fontsize=10)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.xscale("log")
    plt.yscale("log")
    plt.ylabel("Time (ms)", fontsize=10)
    plt.legend(fontsize=10)

    plt.subplot(2, 1, 2)

    plt.plot(n_tests, mems1, label="solve")
    plt.plot(n_tests, mems2, label="inv")
    plt.plot(n_tests, mems3, label="sparse")

    plt.title("Peak Memory Allocation", fontsize=10)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("n", fontsize=10)
    plt.ylabel("Memory (MiB)", fontsize=10)
    plt.legend(fontsize=10)

    plt.savefig("./out/compare_K_solve.pdf")


def generate_K():
    n_tests = [1, 3, 10, 30, 100, 300, 1000, 3000, 10000]
    times1, times2, times3 = [], [], []
    for n_test in n_tests:
        times1.append(generate_K_1(n_test))
        times2.append(generate_K_2(n_test))
        times3.append(generate_K_3(n_test))

    plt.style.use(["science", "ieee", "grid"])
    plt.subplots(1, 1, figsize=(6, 4), dpi=100)

    plt.subplot(1, 1, 1)

    plt.plot(n_tests, times1, label="sparse")
    plt.plot(n_tests, times2, label="numpy")
    plt.plot(n_tests, times3, label="toeplitz")

    plt.title("Time Consumption", fontsize=10)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.xscale("log")
    plt.yscale("log")
    plt.ylabel("Time (ms)", fontsize=10)
    plt.legend(fontsize=10)

    plt.xlabel("n", fontsize=10)

    plt.savefig("./out/compare_K_generation.pdf")


if __name__ == "__main__":
    # generate_K()
    plot()
