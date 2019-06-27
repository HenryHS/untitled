from PIL import Image
import numpy as np

p = Image.open('../data/phone.jpg')

p = np.array(p)

p = 255 - p

print(p, type(p), p.shape)

p = Image.fromarray(p.astype(np.uint8))

p.save('../data/phone3.jpg')
