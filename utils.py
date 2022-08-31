import io
import random
import string
import base64
import cv2
import numpy as np
from PIL import Image


def filter_base64(uri):
    normalized_data = uri.split(',')[1]
    return normalized_data


def base64_to_np_array(base64_uri):
    '''
       - Take in base64 string and return PIL image
       - Convert PIL Image to an RGB image( technically a numpy array ) 
         that's compatible with opencv
    '''
    encoded_data = filter_base64(base64_uri)
    imgdata = base64.b64decode(encoded_data)
    image = Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)


def np_array_to_base64_image(image_array):
    # im_bytes = image_array.tobytes()
    im_b64 = base64.b64encode(image_array)
    return im_b64


def save_image_from_np_array(np_array):
    im = Image.fromarray(np_array)
    img_name = f"{rand_name()}.jpeg"
    im.save(img_name)
    return img_name


def rand_name(length=6):
    return ''.join(random.choices(
        string.ascii_letters, k=length
    ))
