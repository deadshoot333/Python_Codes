from skimage import color
from skimage.filters import try_all_threshold
from util_functions import utils as img
from matplotlib import image
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(__file__))

man_image = image.imread("./images/man.jpg")
man_image_gray = color.rgb2gray(man_image)

fig,ax = try_all_threshold(man_image_gray,verbose=True)

plt.show()