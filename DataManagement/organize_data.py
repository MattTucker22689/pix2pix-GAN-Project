# Splits data up into two groups, training and validation, and renames them

import os
import random
from PIL import Image

directory = "/home/w223u672/GAN_SemanticMap_StyleTransfer/Pix2Pix/data/CompleteDataSet"
# directory = "/home/w223u672/GAN_SemanticMap_StyleTransfer/Pix2Pix/data/CompleteDataSet_wNoise"
directory_train = "/home/w223u672/GAN_SemanticMap_StyleTransfer/Pix2Pix/data/train"
directory_val = "/home/w223u672/GAN_SemanticMap_StyleTransfer/Pix2Pix/data/val"

folder = "Impressionism"
# folder = "Early_Renaissance"
# folder = "Contemporary_Realism"
# folder = "Northern_Renaissance"
# folder = "Rococo"
# folder = "Ukiyo_e"
# folder = "Pop_Art"
# folder = "High_Renaissance"
# folder = "Action_painting"
# folder = "Symbolism"
# folder = "Realism"
# folder = "Romanticism"
# folder = "Cubism"
# folder = "New_Realism"
# folder = "Baroque"
# folder = "Post_Impressionism"
# folder = "Abstract_Expressionism"
# folder = "Pointillism"

directory = directory + "/" + folder

name_val = 0
name_train = 0
for image in os.listdir(directory):
    print(str(image))
    img = Image.open(directory + "/" + image)
    rnd = random.randint(0, 3)
    if rnd == 0:
        img.save(directory_val + "/" + str(name_val) + ".png")
        name_val += 1
        print("Copied to val")
    else:
        img.save(directory_train + "/" + str(name_train) + ".png")
        name_train += 1
        print("Coppied to train")

