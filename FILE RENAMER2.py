import os
import sys
import uuid
from PIL import Image
ttt=1300
os.chdir(r"e:\\ss\\")
lister = os.listdir(os.getcwd())
print(lister)


def scale_image(input_image_path, output_image_path, width=None, height=None):
    original_image = Image.open(input_image_path)
    w, h = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=w, height=h))
    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        raise RuntimeError('Width or height required!')
    original_image.thumbnail(max_size, Image.ANTIALIAS)
    original_image.save(output_image_path)
    scaled_image = Image.open(output_image_path)
    width, height = scaled_image.size
    print('The scaled image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))

i = 0
for kk in lister:
    i += 1
    secr = uuid.uuid4().hex
    os.rename(kk, secr + str(i) + ".jpg")

lister = os.listdir(os.getcwd())
i = 0
for kk in lister:
    i += 1
    scale_image(input_image_path=kk, output_image_path=kk, width=ttt)

lister = os.listdir(os.getcwd())
print(os.getcwd())
os.mkdir("sss")

for kk in lister:
    filename1 = kk
    filename2 = "ans_" + uuid.uuid4().hex + ".jpg"
    file1 = open(filename1, "rb")
    file2 = open(os.getcwd() + "\\sss\\" + filename2, "wb")
    file2.write(file1.read())
    file1.close()
    file2.close()
