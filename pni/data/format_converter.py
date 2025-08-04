from abc import ABC, abstractmethod
from pathlib import Path

class FormatConverter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def convert(self, source_file : str|Path, output_dir: str|Path):
        raise NotImplementedError("Method convert() was not implemented.")