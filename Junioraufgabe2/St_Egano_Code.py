#!/usr/bin/env python3

from PIL import Image
import sys

def St_Egano_Code(image_file):
    image = Image.open(image_file)
    [xsize, ysize] = image.size
    coordinates = [0, 0]
    pixel = image.getpixel(coordinates)
    message = ''
    while pixel[1] + pixel[2] > 0:
        message += chr(pixel[0])
        coordinates = [(pixel[1] + coordinates[0]) % xsize,
                       (pixel[2] + coordinates[1]) % ysize]
        pixel = image.getpixel(coordinates)
    message += chr(pixel[0])
    return message

if __name__ == "__main__":
    print(St_Egano_Code(sys.argv[1]))