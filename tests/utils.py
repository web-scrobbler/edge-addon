from pathlib import Path


def get_filepath(filename: str) -> Path:
    current_script_path = Path(__file__).resolve()
    project_root_dir = current_script_path.parent.parent
    file_path = project_root_dir / filename

    if not file_path.is_file():
        raise FileNotFoundError(f"There is no file named '{filename}' at '{file_path}'")

    return file_path
