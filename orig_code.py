from matplotlib.image import imread 
import numpy as np
import matplotlib.pyplot as plt 
import os

plt.rcParams['figure.figsize'] = [5, 5] 
plt.rcParams.update({'font.size': 18})


A = imread(r"C:\Users\Aadil\Desktop\Sem1 22-23\ELL205 Signals and Systems\Course Project\mona lisa.jpg")  #os.path.join('..', 'DATA', 'AFGHAN3.jpg')) 
B = np.mean (A, -1); # Convert RGB to grayscale

plt.figure()
plt.imshow(A) #, cmap='gray_r')  #(256 - A) for negative image
plt.axis('off')
plt.show()
plt.clf()  #trying to clear the figure

# showing image till here

# Now we will try to compress the image using DFT


Bt = np.fft.fft2 (B)
Btsort = np.sort(np.abs (Bt.reshape(-1))) # sort by magnitude




#Zero out all small coefficients and inverse transform 
for keep in (0.1, 0.05, 0.01, 0.002):
    thresh = Btsort[int (np.floor((1-keep) *len (Btsort)))]
    ind = np.abs(Bt)> thresh #Find small indices
    Btlow = Bt * ind #Zero out small coefficients
    Alow = np.fft.ifft2 (Btlow).real  #Inverse transform
    plt.figure()
    plt.imshow(Alow) #cmap='gray')
    plt.axis('off')
    plt.title('Compressed image: keep = ' + str(keep*100) + '%')
    #plt.show()
   

