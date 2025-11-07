from skimage import color
from skimage.filters import threshold_local
from util_functions import utils 
from matplotlib import image
import os

os.chdir(os.path.dirname(__file__))

cat_image = image.imread("./images/cat.jpg")
cat_image_gray = color.rgb2gray(cat_image)

block_size = 99

local_thresh = threshold_local(cat_image_gray,block_size)

binary_local = cat_image_gray > local_thresh

utils.show_image(binary_local)