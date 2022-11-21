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


def get_all(data: list[dict]) -> str:
    """
    Format all candidates data from json-file to html.
    Args:
        data: all candidates data

    Returns:
        formatted html with candidates data
    """
    html = '<pre>\n'
    for candidate in data:
        html += f"Имя кандидата - {candidate['name']}\n" \
                f"Позиция кандидата - {candidate['position']}\n" \
                f"Навыки - {','.join(candidate['skills'].split(','))}\n\n"
    html += '</pre>'

    return html


def get_by_pk(data: dict) -> str:
    """
    Get a candidate data by primary key
    Args:
        data: all candidates data

    Returns:
        formattedd html with candidate data
    """
    img_url = data['picture']
    html = f'<img src="{img_url}"><br>\n'
    html += get_all([data])

    return html


def get_by_skill(data: list[dict], skill) -> str:
    """
    Get a list of candidates with the required skill
    Args:
        data: all candidates data
        skill: user-selected skill

    Returns:
        formattedd html with list of candidates
    """
    html = '<pre>\n'
    result = ''
    for candidate in data:
        if skill.lower() in candidate['skills'].lower().split(', '):
            result += f"Имя кандидата - {candidate['name']}\n" \
                      f"Позиция кандидата - {candidate['position']}\n" \
                      f"Навыки - {','.join(candidate['skills'].split(','))}\n\n"
    if not result:
        return 'No candidates found for this skill!'

    html += result + '</pre>'

    return html
