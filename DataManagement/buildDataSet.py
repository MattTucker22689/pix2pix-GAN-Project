# Function to stiches two images together

import numpy as np
import os
from PIL import Image, ImageOps

directory_x = "/home/w223u672/GAN_SemanticMap_StyleTransfer/Art_x"
directory_y = "/home/w223u672/GAN_SemanticMap_StyleTransfer/Art_y"
directory_out = "/home/w223u672/GAN_SemanticMap_StyleTransfer/Pix2Pix/data/CompleteDataSet"

if not os.path.exists(directory_out):
    os.makedirs(directory_out)
    print("Made the directory: " + directory_out)

for folder in os.listdir(directory_x):
    # print(str(folder))
    if not folder == ".DS_Store" and not folder == "ReadMe.txt":
        if not os.path.exists(directory_out + "/" + folder):
            os.makedirs(directory_out + "/" + folder)
            print("Made the directory: " + directory_out + "/" + folder)
        for filename in (os.listdir(directory_x + "/" + folder)):
            print(str(filename))
            img_x = Image.open(directory_x + "/" + folder + "/" + filename)
            img_x = img_x.convert('RGB')
            img_x_np = np.asarray(img_x)
            img_x_np = img_x_np.reshape(512, 512, 3)
            # print("img_x shape: " + str(img_x_np.shape))
            img_y = Image.open(directory_y + "/" + folder + "/" + filename)
            img_y = img_y.convert('RGB')
            img_y_np = np.asarray(img_y)
            img_y_np = img_y_np.reshape(512, 512, 3)
            # print("img_y shape: " + str(img_y_np.shape))
            ha, wa = img_x_np.shape[:2]
            hb, wb = img_y_np.shape[:2]
            # ha, wa = 512, 512
            # hb, wb = 512, 512
            max_height = np.max([ha, hb])
            total_width = wa + wb
            img_out_np = np.zeros(shape=(max_height, total_width, 3))
            # print("img_out_np shape: " + str(img_out_np.shape))
            img_out_np[:ha, :wa] = img_x_np
            img_out_np[:hb, wa:wa + wb] = img_y_np
            # img_out_np[:ha, :wa] = img_x
            # img_out_np[:hb, wa:wa + wb] = img_y
            # print("img_out_np: " + str(img_out_np))
            img_out = Image.fromarray((img_out_np * 255).astype(np.uint8))
            # img_out = Image.fromarray(img_out_np, 'RGB')
            img_out = ImageOps.invert(img_out)
            img_out.save(directory_out + "/" + folder + "/" + filename)