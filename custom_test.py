import glob
from IPython.display import Image, display

i = 0
limit = 10000  # max images to print
for imageName in glob.glob('/content/yolov7/runs/detect/exp/*.jpg'):  # assuming JPG
    if i < limit:
        display(Image(filename=imageName))
        print("\n")
    i = i + 1
