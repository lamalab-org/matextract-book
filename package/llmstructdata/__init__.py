
import matplotlib as mpl
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import warnings
import litellm
from litellm.caching import Cache

litellm.cache = Cache()

mpl.style.use("book.mplstyle")

load_dotenv("../../.env", override=True)

warnings.filterwarnings("ignore")
