from pni.data.format_converter import FormatConverter
import numpy as np
from cellpose.io import imread
from cellpose import models
from pni.utils import prepare_paths

class Tif2Array(FormatConverter):
    def __init__(self, gpu = False):
        print("Loading cellpose model:")
        self._model = models.CellposeModel(gpu=gpu)


    def convert(self, source_file, output_dir):
        source_file, output_dir = prepare_paths(source_file, output_dir)
        img = imread(source_file)
        
        masks, _, _ = self._model.eval(img, diameter=None)

        mask_npy_path = output_dir / (source_file.stem + ".npy")
        np.save(mask_npy_path, masks)
        print(f"Mask saved: {mask_npy_path.name}")

