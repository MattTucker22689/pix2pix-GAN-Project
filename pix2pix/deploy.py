import numpy as np
import torch
import config
from PIL import Image
from generator_model import Generator
import torch.optim as optim
from torchvision.utils import save_image

model = Generator(in_channels=3, features=64).to(config.DEVICE)

checkpoint = torch.load('gen.pth.tar', map_location=torch.device('cpu')) #12hrs_wNoise_gen.pth.tar
model.load_state_dict(checkpoint['state_dict'])

model.eval()

# Images: 2896.png 3617.png 3628.png 4096.png 4099.png 4490.png 4554.png 5748.png
# img_in = Image.open('/home/w223u672/GAN_SemanticMap_StyleTransfer/Pix2Pix/data/val/4490.png')
# img_in = img_in.convert('RGB') 
# img_in_ar = np.array(img_in)
# img_out_np = np.zeros(shape=(512, 512, 3))
# img_np_temp = img_in_ar[:512, :512]
# img_temp = Image.fromarray(img_np_temp)
# img_temp = img_temp.resize((256, 256))
# img_np = np.array(img_temp)

############################################################
# WuShock Example
# Images: scrible.png WuShock_big_reduced.png
img_in = Image.open('/home/w223u672/GAN_SemanticMap_StyleTransfer/Pix2Pix/data/val/scrible.png')
img_in = img_in.convert('RGB') 
img_in_ar = np.array(img_in)
img_temp = Image.fromarray(img_in_ar)
img_temp = img_temp.resize((256, 256))
img_np = np.array(img_temp)
############################################################

input_image = config.transform_only_input(image=img_np)["image"]
input_image = torch.unsqueeze(input_image, dim=-4) # dim = 0 # dim = -4

# Range 1-3
for i in range(1):
    input_image = model(input_image)
results = input_image * 0.5 + 0.5  # remove normalization
save_image(results, "evaluation/deploy_demo.png")
