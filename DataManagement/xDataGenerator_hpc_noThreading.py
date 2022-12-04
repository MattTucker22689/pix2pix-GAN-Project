import os
from PIL import Image, ImageFilter
from PIL.Image import Quantize
import time

def processImage(img, dest):

    # img = img.convert('RGB')

    # Reduces images to 16 colors
    #img = img.quantize(16, method=Quantize.MAXCOVERAGE, kmeans=16)

    img = img.convert('RGB')
    # Adds Gaussian Blur to image
    img = img.filter(ImageFilter.GaussianBlur(radius=4))
    # Reduces images to 4 colors
    img = img.quantize(4, method=Quantize.MAXCOVERAGE, kmeans=4)

    img.save(dest)

def main():
    # Set directory

    # directory_in = "C:/Users/Owner/Desktop/Stats_Project_Code/Art_Inputs"
    # directory_out = "C:/Users/Owner/Desktop/Stats_Project_Code/Art_x"

    directory_in = "/home/w223u672/GAN_SemanticMap_StyleTransfer/Art_Resized"
    directory_out = "/home/w223u672/GAN_SemanticMap_StyleTransfer/Art_x"

    if not os.path.exists(directory_out):
        os.makedirs(directory_out)
        print("Made the directory: " + directory_out)

    for folder in os.listdir(directory_in):
        if not folder == ".DS_Store" and not folder == "ReadMe.txt":
            if not os.path.exists(directory_out + "/" + folder):
                os.makedirs(directory_out + "/" + folder)
                print("Made the directory: " + directory_out + "/" + folder)
            for filename in (os.listdir(directory_in + "/" + folder)):
                print(str(filename))
                image = Image.open(directory_in + "/" + folder + "/" + filename)
                destination = directory_out + "/" + folder + "/" + filename
                processImage(image, destination)

if __name__ == "__main__":
    initial_time = time.time()
    main()
    print("\n\n\n\n\nTime taken: " + str(time.time() - initial_time))
