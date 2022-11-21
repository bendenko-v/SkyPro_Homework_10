from __future__ import annotations

import json


def load_candidates(path) -> list | None:
    """
    Load data from json-file

    Args:
        path (str): path to file
    Returns:
        data (list): list with data if successful
        None: if raises FileNotFoundError
    Raises:
        FileNotFoundError: if the file is not found
    """
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return None
