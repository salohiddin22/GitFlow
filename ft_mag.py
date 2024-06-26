import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the image as grayscale
gray = cv2.imread("im/11.jpg", cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded correctly
if gray is None:
    raise ValueError("Image not found or unable to load.")

# Step 2: Compute the 2D Fourier transform of the image
f_transform = np.fft.fft2(gray)

# Step 3: Shift the zero frequency component to the center
f_transform_shifted = np.fft.fftshift(f_transform)

# Step 4: Compute the magnitude spectrum
magnitude_spectrum = np.abs(f_transform_shifted)

# Step 5: Normalize the magnitude spectrum for visualization
magnitude_spectrum_normalized = np.log1p(magnitude_spectrum)  # Use log scale for better visualization
magnitude_spectrum_normalized = cv2.normalize(magnitude_spectrum_normalized, None, 0, 255, cv2.NORM_MINMAX)

# Convert the normalized magnitude spectrum to an 8-bit image
magnitude_spectrum_normalized = magnitude_spectrum_normalized.astype(np.uint8)

# Step 6: Save the magnitude spectrum image
cv2.imwrite('ftt_spectrum.png', magnitude_spectrum_normalized)

# Optionally, display the magnitude spectrum
plt.imshow(magnitude_spectrum_normalized, cmap='gray')
plt.colorbar()
plt.title('Fourier Transform Magnitude Spectrum')
plt.show()
