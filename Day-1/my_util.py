from pathlib import WindowsPath


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
