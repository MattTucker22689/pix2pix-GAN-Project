# pix2pix-GAN-Project
The following repository is of a project I did for a Stats course, STAT 571 Statistical Methods I, which I took for graduate credit.

In it you will find 6 files, dataset.py, config.py, train.py, utils.py, discriminator_model.py, and generator_model.py which I can 
not claim as my own. It was orignally built by Aladin Persson and can be found at:
  https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/GANs/Pix2Pix

You will also find several files which clean and generate the data set as well as to deploy the trained model, all of which were built 
by me.

The purpose of the project, was to demonstrate an ability to apply the topics of the course, while learning and applying new material
to achive some goal. In particualar, we set out to learn the mathematics behind GANs and implement a demonstration of a GAN.

# To run:
- You will need to add the folders "data\" and "evaluation\" to "\pix2pix\."
- You will also need to add "training\" and "val\ to "\pix2pix\data\."
- You will need to populate the folder "\pix2pix\data\training\" with training data
- You will need to add validation data the folder "\pix2pix\data\val\" folder
- You will need to train the model by running "train.py" in "\pix2pix\"
- Once trained, to deploy the model, run "deploy.py" in "\pix2pix\"

# Notes:
- Modification to some of the files may be neccesary depending on where I am in steralizing the file when you download 
the repo.
- For this project we used the WikiArt data set which can be found here:
https://archive.org/details/wikiart-dataset
