from skimage import exposure
from util_functions import utils
from matplotlib import image
import os 

os.chdir(os.path.dirname(__file__))
xray = image.imread("./images/chest_xray_image.png")

image_eq = exposure.equalize_hist(xray)

utils.plot_comparison(xray,image_eq,"After Histogram Equalization")