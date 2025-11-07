from skimage import color
from util_functions import utils as img
from skimage.filters import try_all_threshold
from matplotlib import image
import matplotlib.pyplot as plt
import os 

os.chdir(os.path.dirname(__file__))
shrimp = image.imread("./images/shrimp_gill.jpg")

gray_shrimp = color.rgb2gray(shrimp)

# img.show_image(gray_shrimp,"Grayscale conversion")

# print(type(gray_shrimp))
# plt.hist(gray_shrimp.ravel(),bins=256)
# plt.show()
fig,ax = try_all_threshold(gray_shrimp,verbose=True)
plt.show()