from pni.data.lif2tif import Lif2Tif
from pni.common import TMP_DIR

lif2tif = Lif2Tif()
lif2tif.convert("example_data/ARPE19_nic_48H_01.lif",TMP_DIR)