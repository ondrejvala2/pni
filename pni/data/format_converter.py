from abc import ABC, abstractmethod

class FormatConverter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def convert(self, source_file, output_dir):
        raise NotImplementedError("Method concert() was not implemented.")