from typing import List
from pathlib import Path
from typing import Tuple
import os

def get_files_from_dir(dir_path: Path, suffix: str) -> List[Path]:
    """
    Returns a list of files in the specified directory with the given suffix.
    
    Parameters:
        dir_path (Path): Path to the directory to search.
        suffix (str): File suffix to match (e.g. '.txt').

    Returns:
        List[Path]: List of Path objects representing matching files.
    """
    return [file for file in dir_path.iterdir() if file.is_file() and file.suffix == suffix]

def prepare_paths(source_file : str|Path, output_dir: str|Path) -> Tuple[Path, Path]:
    source_file = Path(source_file)
    output_dir = Path(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    return source_file, output_dir