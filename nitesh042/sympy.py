
from skimage import io
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftfreq, ifft
from scipy import ndimage as nd
from scipy.fft import fft, ifft
from scipy import fftpack
img = io.imread("D:\dips\img.jpg")
plt.imshow(img)
plt.show()
img_fft =  fftpack.fft2(img)


# inverse of signal
img_ifft = fftpack.ifft2(img_fft).real

plt.figure(figsize=(10,10))

plt.subplot(131)
plt.imshow(img)
plt.title("Original")

plt.subplot(132)
plt.title("Spectrum")
plt.imshow(img_fft.astype(np.uint8))
plt.subplot(133)

plt.title("Reconstructed")
plt.imshow(img_ifft.astype(np.uint8))
plt.show()
