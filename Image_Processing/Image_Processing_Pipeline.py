import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
from util_functions import utils as img
from skimage import color, transform, restoration, filters, segmentation, morphology
from skimage.filters import threshold_otsu
import os

os.chdir(os.path.dirname(__file__))
grass = image.imread("./images/grass_image.jpg")
##size of the image
print(grass.shape[:2])

img.show_image(grass,"Grass RGB")

grass_gray = color.rgb2gray(grass)

img.show_image(grass_gray,"Grass Grayscale")

grass_resized = transform.resize(grass_gray,(256,256),anti_aliasing=True)

img.show_image(grass_resized,"Grass Resized")

grass_denoised = restoration.denoise_tv_chambolle(grass_resized,weight=0.1)

img.show_image(grass_denoised,"Grass Denoised")

grass_edges = filters.sobel(grass_denoised)

img.show_image(grass_edges,"Grass Edges Detected")

threshold = threshold_otsu(grass_denoised)
binary = grass_denoised > threshold

img.show_image(binary,"Grass Segmented")

