from skimage.color import rgb2gray
from skimage import morphology
from util_functions import utils
from matplotlib import image 
from skimage.filters import threshold_otsu 
import os 

os.chdir(os.path.dirname(__file__))
man_image = image.imread("./images/man.jpg")
man_gray = rgb2gray(man_image)

thresh = threshold_otsu(man_gray)

binary_global = man_gray > thresh 
square = morphology.square(12)

eroded_image = morphology.binary_erosion(binary_global,footprint=square)
utils.plot_comparison(binary_global,eroded_image,"Erosion with 12X12 square structuring element")