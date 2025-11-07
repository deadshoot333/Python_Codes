import matplotlib.pyplot as plt 
import os 

os.chdir(os.path.dirname(__file__)) ## change the working directory at runtime, Sets working directory to script location
cat = plt.imread("./images/cat.jpg")## loading the image using matplotlib for numpy array

# print(type(cat))

##obtaining the red values of the image
red_channel = cat[:,:,0]
plt.imshow(red_channel)
plt.title("Red Channel")
plt.show()

## obtaining the green values of the image
green_channel = cat[:,:,1]
plt.imshow(green_channel)
plt.title("Green Channel")
plt.show()

## obtaining the blue values of the image
blue_channel = cat[:,:,2]
plt.imshow(blue_channel)
plt.title("Blue Channel")
plt.show()