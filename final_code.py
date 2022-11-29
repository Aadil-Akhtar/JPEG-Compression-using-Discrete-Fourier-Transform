#JPEG compression using DFT

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
import os

# Read the image

im = Image.open(r"C:\Users\Aadil\Desktop\Sem1 22-23\ELL205 Signals and Systems\Course Project\mona lisa.jpg")


# Convert to 8-bit grayscale
im = im.convert('L')

# Convert to 64-bit float
im = np.array(im, dtype=np.float64)

# Compute DCT
im_dct = dct(dct(im.T, norm='ortho').T, norm='ortho')

# Quantization
thresh = 10
im_dct_q = np.round(im_dct/thresh)*thresh

# Inverse DCT
im_dct_q_idct = idct(idct(im_dct_q.T, norm='ortho').T, norm='ortho')

# Display the results
plt.figure()
print('\n\n')
print("Original image file size: ", os.path.getsize(r"C:\Users\Aadil\Desktop\Sem1 22-23\ELL205 Signals and Systems\Course Project\mona lisa.jpg"), "bytes")

plt.imshow(im, cmap='gray')
plt.title('Original image')
plt.figure()
print("Compressed image file size: ", os.path.getsize(r"C:\Users\Aadil\Desktop\Sem1 22-23\ELL205 Signals and Systems\Course Project\Compressed_Mona_Lisa.png"), "bytes")
plt.imshow(im_dct_q_idct, cmap='gray')
plt.title('Threshold=10')
plt.show()