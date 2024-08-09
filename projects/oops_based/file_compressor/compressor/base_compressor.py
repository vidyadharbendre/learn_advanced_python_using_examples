# compressor/base_compressor.py
from abc import ABC, abstractmethod

class BaseCompressor(ABC):

    @abstractmethod
    def compress(self, input_path, output_path):
        pass
