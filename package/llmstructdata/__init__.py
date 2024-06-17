import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
import pystow

url = "https://raw.githubusercontent.com/lamalab-org/plotutils/main/kevin.mplstyle"
path = pystow.ensure("matstructdata", "plotsettings", url=url)

mpl.style.use(path)

warnings.filterwarnings("ignore")
