import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the image as grayscale
gray = cv2.imread("im/11.jpg", cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded correctly
if gray is None:
    raise ValueError("Image not found or unable to load.")

# Step 2: Compute gradients in x and y directions using Sobel filter
grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Step 3: Compute the gradient magnitude
gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)

# Normalize the gradient magnitude for visualization
gradient_magnitude_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)

# Convert the normalized gradient magnitude to an 8-bit image
gradient_magnitude_normalized = gradient_magnitude_normalized.astype(np.uint8)

# Step 4: Save the gradient magnitude image
cv2.imwrite('gradient_map.png', gradient_magnitude_normalized)

# Optionally, display the gradient magnitude map
plt.imshow(gradient_magnitude_normalized, cmap='gray')
plt.colorbar()
plt.title('Gradient Magnitude Map')
plt.show()

#this is just for testing
