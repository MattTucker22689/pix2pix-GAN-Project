# Function to add noise to domain data an stitch two images together
import random

import numpy as np
import os
from PIL import Image, ImageOps

directory_x = "/home/w223u672/GAN_SemanticMap_StyleTransfer/Art_x"
directory_y = "/home/w223u672/GAN_SemanticMap_StyleTransfer/Art_y"
directory_out = "/home/w223u672/GAN_SemanticMap_StyleTransfer/Pix2Pix/data/CompleteDataSet_wNoise"

if not os.path.exists(directory_out):
    os.makedirs(directory_out)
    print("Made the directory: " + directory_out)

for folder in os.listdir(directory_x):
    if not folder == ".DS_Store" and not folder == "ReadMe.txt":
        if not os.path.exists(directory_out + "/" + folder):
            os.makedirs(directory_out + "/" + folder)
            print("Made the directory: " + directory_out + "/" + folder)
        for filename in (os.listdir(directory_x + "/" + folder)):
            print(str(filename))
            img_x = Image.open(directory_x + "/" + folder + "/" + filename)
            img_x = img_x.convert('RGB')
            img_x_np = np.array(img_x)
            img_x_np = img_x_np.reshape(512, 512, 3)
            img_x_np_shaped = img_x_np.reshape(512*512, 3)
            for i in range(512*512):
                rnd = random.randint(0, 3)
                if rnd == 0:
                    tupl = (np.random.randint(0, 255, size=3))
                    img_x_np_shaped[i] = tupl
            img_x_np = img_x_np_shaped.reshape(512, 512, 3)
            img_y = Image.open(directory_y + "/" + folder + "/" + filename)
            img_y = img_y.convert('RGB')
            img_y_np = np.array(img_y)
            img_y_np = img_y_np.reshape(512, 512, 3)
            ha, wa = img_x_np.shape[:2]
            hb, wb = img_y_np.shape[:2]
            max_height = np.max([ha, hb])
            total_width = wa + wb
            img_out_np = np.zeros(shape=(max_height, total_width, 3))
            img_out_np[:ha, :wa] = img_x_np
            img_out_np[:hb, wa:wa + wb] = img_y_np
            img_out = Image.fromarray((img_out_np * 255).astype(np.uint8))
            img_out = ImageOps.invert(img_out)
            print("img_out_np shape: " + str(img_out_np.shape))
            print("img_out_np: " + str(img_out_np))
            img_out.save(directory_out + "/" + folder + "/" + filename)
