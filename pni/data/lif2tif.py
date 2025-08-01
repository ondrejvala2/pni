from pni.data.format_converter import FormatConverter
import liffile
import tifffile
import numpy as np
import os

class Lif2Tif(FormatConverter):
    def convert(self, source_file, output_dir):
        """
        Converts a .lif file to .tif files.
        Each series within the .lif file will be saved as a separate multi-page TIFF.
    
        Args:
            lif_path (str): Path to the input .lif file.
            output_dir (str): Directory to save the output .tif files.
        """
        os.makedirs(output_dir, exist_ok=True)

        try:
            lif_file = liffile.LifFile(source_file)
            for i, lif_image in enumerate(lif_file.images):
                print(f"Processing series {i}: {lif_image.name}")

                full_image_data = lif_image.asarray()

                _, h, w = full_image_data.shape
                combined_image = np.zeros((h, w, 3), dtype=full_image_data.dtype)

                combined_image[:, :, 1] = full_image_data[1]
                combined_image[:, :, 2] = full_image_data[0]

                base_name = (
                    lif_image.name.replace(" ", "_").replace("/", "_").replace("\\", "_")
                )  # Clean up name for filename
                # Add a unique identifier if the base name is not unique (e.g., if multiple series have the same name)
                output_tif_path = os.path.join(output_dir, f"{base_name}_series{i}.tif")

                tifffile.imwrite(
                    output_tif_path,
                    combined_image,
                    imagej=True,
                    ome=True,
                )

                print(f"Saved {output_tif_path}")

        except Exception as e:
            print(f"An error occurred: {e}")


