import matplotlib as mpl  # noqa:F401
import matplotlib.pyplot as plt  # noqa:F401
from dotenv import load_dotenv
import warnings
import litellm
from litellm.caching import Cache
import pystow

litellm.cache = Cache()

url = "https://raw.githubusercontent.com/lamalab-org/plotutils/main/kevin.mplstyle"
path = pystow.ensure("matstructdata", "plotsettings", url=url)

load_dotenv("../../.env", override=True)

warnings.filterwarnings("ignore")

__all__ = ["mpl", "plt", "path"]
