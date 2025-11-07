from skimage import exposure
from util_functions import utils
from matplotlib import image
import os 

os.chdir(os.path.dirname(__file__))
aerial = image.imread("./images/image_aerial.tiff")

image_adapteq = exposure.equalize_adapthist(aerial,clip_limit=0.03)

utils.plot_comparison(aerial,image_adapteq,"After Adaptive Histogram Equalization")