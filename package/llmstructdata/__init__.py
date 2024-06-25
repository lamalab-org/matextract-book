from os.path import (
    join,
    dirname
)
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
from dotenv import (
    load_dotenv,
    find_dotenv,
)
import warnings

mpl.style.use("book.mplstyle")

# First and second are equivalent
# Start by trying the most basic one
load_dotenv(find_dotenv(sys.path[1]))
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path, override=True)
# load_dotenv(".env", override=True)


warnings.filterwarnings("ignore")
