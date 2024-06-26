import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the image
gray = cv2.imread("im/11.jpg", cv2.IMREAD_GRAYSCALE)
# print(gray)

# Step 2: Convert to grayscale
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Compute gradients in x and y directions using Sobel filter
grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Step 4: Compute the angle map
angle_map = np.arctan2(grad_y, grad_x)

# Convert angles from radians to degrees
angle_map_degrees = np.degrees(angle_map)

# Normalize the angle map for visualization
angle_map_normalized = cv2.normalize(angle_map_degrees, None, 0, 255, cv2.NORM_MINMAX)

# Convert the normalized angle map to an 8-bit image
angle_map_normalized = angle_map_normalized.astype(np.uint8)
am_3chan = gray_image_3channel = cv2.merge((angle_map_normalized, angle_map_normalized, angle_map_normalized))

hsv_image = cv2.cvtColor(am_3chan, cv2.COLOR_BGR2HSV)
cv2.imwrite('am_11_hsv.png', hsv_image)
cv2.imwrite('am_11.png', angle_map_normalized)

# Display the angle map
plt.imshow(angle_map_normalized, cmap='hsv')
plt.colorbar()
plt.title('Angle Map')
plt.show()
