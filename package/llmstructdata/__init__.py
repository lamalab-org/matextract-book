import matplotlib as mpl
import matplotlib.pyplot as plt
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
