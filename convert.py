from PIL import Image
import os,glob

# Update this variable with the file path to the images you need to convert: 
PATH = './photos'
# Choose the extension you want to convert from, loop will only grab files with that extension
CURRENT_EXTENSION = '*.webp'

# Loop through images that have 'CURRENT_EXTENSION'
for filename in glob.glob(os.path.join(PATH, CURRENT_EXTENSION)):
    # Open the images
    with open(filename, 'r') as f:
        # convert color profile
        im = Image.open(filename).convert("RGB")
        im.save(str(filename)[:-5] + ".jpg", "jpeg")
        
# Huge thank you to Ajeet Verma for this excellent post:
# https://medium.com/@ajeet214/image-type-conversion-jpg-png-jpg-webp-png-webp-with-python-7d5df09394c9
