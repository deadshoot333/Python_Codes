from skimage import color
from util_functions import utils as img
from matplotlib import image
import os 

os.chdir(os.path.dirname(__file__)) ## change the working directory at runtime, Sets working directory to script location
cat = image.imread("./images/cat.jpg")

gray_cat = color.rgb2gray(cat)

img.show_image(gray_cat,"Gray Cat")