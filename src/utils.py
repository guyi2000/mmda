#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   utils.py
@Time    :   2023/06/25 16:32:11
@Author  :   MPCB_Bishop
@Version :   1.0
@Contact :   guy22@mails.tsinghua.edu.cn
@License :   (C)Copyright 2022-2023, MPCB_Bishop
@Desc    :   Some utilities for time & memory analysis.
             You should install colorama first.
"""

import colorama
import functools
import tracemalloc

from timeit import timeit
from colorama import Fore, Style

from typing import Callable, List, Tuple, Any

colorama.init()


def _func_time_mon(func: Callable, duration: float = 5.0) -> Tuple[float, int]:
    """
    Measure the execution time of a function `func`
    by running it repeatedly for a certain duration.

    Parameters
    ----------
    func : Callable
        The function to be timed.
    duration : float, optional
        The duration in seconds for which the function should be run repeatedly,
        by default 5.0

    Returns
    -------
    Tuple[float, int]
        A tuple containing the average execution time of the function in milliseconds,
        and the number of times the function was run.
    """
    test_time = timeit(func, number=1)
    number = int(duration / test_time) + 1
    if number > 10:
        test_time = timeit(func, number=number) / number * 1000
    else:
        number = 1
        test_time *= 1000
    return test_time, number


def _func_mem_mon(func: Callable) -> float:
    """
    Measure the peak memory usage of a function `func`
    by running it and using the tracemalloc module.

    Parameters
    ----------
    func : Callable
        The function to be measured.

    Returns
    -------
    float
        The peak memory usage of the function in MiB.
    """
    tracemalloc.start()
    func()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 2**20


def time_mon(func: Callable) -> Callable:
    """
    A decorator that measures the peak memory usage of a function `func`
    and prints the result.

    Parameters
    ----------
    func : Callable
        The function to be decorated.

    Returns
    -------
    Callable
        The decorated function that measures the peak memory usage of `func`.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        test_time, number = _func_time_mon(lambda: func(*args, **kwargs))
        print(
            f"{Fore.GREEN}{Style.BRIGHT}[INFO]{Style.RESET_ALL}\t"
            f" Function [{Fore.RED}{Style.BRIGHT}{func.__name__}{Style.RESET_ALL}]"
            f" finished in {Fore.GREEN}{Style.BRIGHT}{test_time:.4f}{Style.RESET_ALL}"
            f" ms, called {Fore.GREEN}{Style.BRIGHT}{number}{Style.RESET_ALL} times."
        )
        return test_time

    return wrapper


def mem_mon(func: Callable) -> Callable:
    """
    A decorator that measures the execution time of a function `func`
    and prints the result.

    Parameters
    ----------
    func : Callable
        The function to be decorated.

    Returns
    -------
    Callable
        The decorated function that measures the execution time of `func`.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        peak = _func_mem_mon(lambda: func(*args, **kwargs))
        print(
            f"{Fore.GREEN}{Style.BRIGHT}[INFO]{Style.RESET_ALL}\t"
            f" Function [{Fore.RED}{Style.BRIGHT}{func.__name__}{Style.RESET_ALL}]"
            f" allocated {Fore.GREEN}{Style.BRIGHT}{peak:.4f}{Style.RESET_ALL}"
            f" MiB memory (peak)."
        )
        return peak

    return wrapper


def auto_mon_with_n(
    func: Callable[[int], Any],
    n_tests: List[int],
    duration: float = 60,
) -> Tuple[List[float], List[float]]:
    """
    Automatically measure the execution time and memory usage of a function `func`
    for different input sizes.

    Parameters
    ----------
    func : Callable[[int], Any]
        The function to be measured.
    n_tests : List[int]
        A list of input sizes to test `func` with.
    duration : float, optional
        The total duration in seconds for total tested, by default 60

    Returns
    -------
    Tuple[List[float], List[float]]
        A tuple containing two lists:
        the list of execution times (in milliseconds) for each input size,
        and the list of peak memory usage (in MiB) for each input size.
    """
    duration /= len(n_tests)
    return (
        [_func_time_mon(lambda: func(n), duration)[0] for n in n_tests],
        [_func_mem_mon(lambda: func(n)) for n in n_tests],
    )


__all__ = ["time_mon", "mem_mon", "auto_mon_with_n"]
