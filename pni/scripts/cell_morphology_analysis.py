from pni.data.lif2tif import Lif2Tif
from pni.data.tif2array import Tif2Array
from pni.common import TMP_DIR
from pni.utils import get_files_from_dir
from tqdm import tqdm

lif2tif = Lif2Tif()
lif2tif.convert("example_data/ARPE19_nic_48H_01.lif",TMP_DIR)

tif2array = Tif2Array()
[tif2array.convert(tif_file,TMP_DIR) for tif_file in tqdm(get_files_from_dir(TMP_DIR,"tif"), desc="Detecting cells in tif")]
