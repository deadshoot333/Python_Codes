from skimage import color
from skimage.filters import threshold_otsu ## used otsu algo 
from Image_Processing.util_functions import utils as img
from matplotlib import image
import os

os.chdir(os.path.dirname(__file__))
man_image = image.imread("./images/man.jpg")
man_image = color.rgb2gray(man_image)
thresh = threshold_otsu(man_image)

binary_global = man_image > thresh 

img.show_image(binary_global,"Global Thresholding")