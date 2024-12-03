from pathlib import WindowsPath
import numpy as np


def load_data(file_path: WindowsPath):
    """
    Loads data from a file (JSON or CSV) into a dictionary.

    Parameter:
        file_path (WindowsPath): Path to the file.

    Returns:
        misc_util.result_message: A dictionary containing:
            - result (bool): Status of the operation.
            - message (str): Success or error message.
            - payload (dict): Parsed file data or an empty string on failure.
    """

    try:
        if "txt" in file_path:
            with open(file_path, "r") as handle:
                files = handle.readlines()
    except FileNotFoundError as e:
        return f"{e}"
    except IOError as e:
        return f"{e}"
    except Exception as e:
        return f"{e}"
    else:
        return files


def read_all(file_path: WindowsPath):
    try:
        if "txt" in file_path:
            with open(file_path, "r") as handle:
                files = handle.read()
    except FileNotFoundError as e:
        return f"{e}"
    except IOError as e:
        return f"{e}"
    except Exception as e:
        return f"{e}"
    else:
        return files


def is_increasing_or_decreasing(lst):
    arr = np.array(lst)

    arr = arr.astype(int)

    diff = np.diff(arr)

    increasing_or_decreasing = np.all(diff > 0) or np.all(diff < 0)

    return increasing_or_decreasing


def is_true(num1: str, num2: str):
    result = int(num1) - int(num2)
    if abs(result) in [1, 2, 3]:
        return True
    else:
        return False


def is_safe(val):
    comparisons = [is_true(val[i], val[i + 1])
                   for i in range(len(val) - 1)]
    return comparisons
