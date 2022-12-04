# Function to rename multiple files
#Only run once, any more than that and you will delete files due to duplicated names

import os
from PIL import Image

directory_in = "/home/w223u672/GAN_SemanticMap_StyleTransfer/Art_Inputs"
directory_out = "/home/w223u672/GAN_SemanticMap_StyleTransfer/Art_Resized"

if not os.path.exists(directory_out):
    os.makedirs(directory_out)
    print("Made the directory: " + directory_out)
    
for folder in os.listdir(directory_in):
    #print(str(folder))
    if not folder == ".DS_Store" and not folder == "ReadMe.txt":
        if not os.path.exists(directory_out + "/" + folder):
            os.makedirs(directory_out + "/" + folder)
            print("Made the directory: "+ directory_out + "/" + folder)
        for filename in (os.listdir(directory_in + "/" + folder)):
            print(str(filename)) 
            img = Image.open(directory_in + "/" + folder + "/" + filename)
            img = img.resize((512,512))
            img.save(directory_out + "/" + folder + "/" + filename)
