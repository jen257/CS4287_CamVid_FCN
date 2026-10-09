import os
# Core Paths (Specifies the root directory of the dataset)
DATA_DIR = "./CamVid"

# Image & Model Dimensions (Bridge between data and model)
IMG_HEIGHT = 360
IMG_WIDTH = 480
NUM_CLASSES = 12  # CamVid default 11 object classes + 1 background class

# Initial Training Parameters (Variables most frequently modified during tuning)
BATCH_SIZE = 8
LEARNING_RATE = 1e-4
EPOCHS = 50
