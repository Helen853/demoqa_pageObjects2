from pathlib import Path


def take_path(relative_path: str):
    path = str(Path(__file__).parent.parent.parent.joinpath('resources').joinpath(relative_path))
    return path