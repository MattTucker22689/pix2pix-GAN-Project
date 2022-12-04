# pix2pix-GAN-Project
The following repository is of a project I did for a Stats course, STAT 571 Statistical Methods I, which I took for graduate credit.

In it you will find 6 files, dataset.py, config.py, train.py, utils.py, discriminator_model.py, and generator_model.py which I can 
not claim as my own. It was orignally built by Aladin Persson and can be found at:
  https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/GANs/Pix2Pix

You will also find several files which clean and generate the data set as well as to deploy the trained model, all of which were built 
by me.

The purpose of the project, was to demonstrate an ability to apply the topics of the course, while learning and applying new material
to achive some goal. In particualar, we set out to learn the mathematics behind GANs and implement a demonstration of a GAN.

Structure of Repo:

root\
|
|
- README.md
--- DataManagement\
  |
  |
  - buildDataSet_wNoise.py
  - buildDataSet.py
  - organize_data.py
  - resize.py
  - xDataGenerator_hpc_noThreading.py
--- pix2pix\
  |
  |
  - config.py
  - dataset.py
  - deploy.py
  - discriminator_model.py
  - generator_model.py
  - run_training.slurm
  - train.py
  - utils.py
  --- evaluation\
    - EMPTY
  --- data\
    --- training\
      - EMPTY
    --- val\
      - Empty
