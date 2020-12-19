from os.path import join, dirname, abspath
from pathlib import Path 

RESOLUTION = int(1e3)
SRC_PATH = dirname(abspath(__file__))
CACHE_PATH = join(SRC_PATH, 'cached')
PROJECT_ROOT_PATH = Path(__file__).parent.parent 
FIG_PATH = join(PROJECT_ROOT_PATH, 'figs')
