import math
from PIL import Image, ImageDraw

from . import util



class ARRANGE():

    def get_size(self, image):
        img_size = image.size
        return img_size
    
    def arange(self, image, target_size_2d, base_size):
