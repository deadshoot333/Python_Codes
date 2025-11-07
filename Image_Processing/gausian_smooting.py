from skimage.filters import gaussian
from util_functions import utils
from matplotlib import image
import os

os.chdir(os.path.dirname(__file__))
cat_image = image.imread("./images/cat.jpg")

gaussian_image = gaussian(cat_image)

utils.plot_comparison(cat_image,gaussian_image,"Blurred with Gausian Filter")
