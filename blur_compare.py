import cv2
import numpy as np
import os

# Path to the test image
image_path = "test_images/Plant.jpeg"

# Load the image
image = cv2.imread(image_path)

# Check that the image loaded correctly
if image is None:
    print("ERROR: Image could not be loaded.")
else:
    print("Image loaded successfully!")
    print("Image size:", image.shape)
    # Apply a spatial Gaussian blur
spatial_blur = cv2.GaussianBlur(image, (15, 15), 0)

# Save the blurred image
cv2.imwrite("results/spatial_blur.jpg", spatial_blur)

print("Spatial blur created and saved successfully!")
# Convert image to grayscale for Fourier processing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a Gaussian kernel
kernel_size = 15
sigma = 3

gaussian_1d = cv2.getGaussianKernel(kernel_size, sigma)
gaussian_2d = gaussian_1d @ gaussian_1d.T

# Pad the kernel so it matches the image size
padded_kernel = np.zeros_like(gray, dtype=np.float32)

kh, kw = gaussian_2d.shape
padded_kernel[:kh, :kw] = gaussian_2d

# Shift kernel so its center is at the origin
padded_kernel = np.roll(padded_kernel, -kh // 2, axis=0)
padded_kernel = np.roll(padded_kernel, -kw // 2, axis=1)

# Fourier transform of image and filter
image_fft = np.fft.fft2(gray)
kernel_fft = np.fft.fft2(padded_kernel)

# Multiply in the frequency domain
frequency_result = image_fft * kernel_fft

# Convert back to spatial domain
fourier_blur = np.fft.ifft2(frequency_result)
fourier_blur = np.real(fourier_blur)

# Clip values and convert back to 8-bit image
fourier_blur = np.clip(fourier_blur, 0, 255).astype(np.uint8)

# Save Fourier-domain result
cv2.imwrite("results/fourier_blur.jpg", fourier_blur)

print("Fourier-domain blur created and saved successfully!")
# ---------------------------------------------------------
# VALIDATION: Compare spatial convolution and Fourier result
# ---------------------------------------------------------

# Convert grayscale image to floating point
gray_float = gray.astype(np.float32)

# Spatial-domain convolution using the SAME Gaussian kernel
spatial_equivalent = cv2.filter2D(
    gray_float,
    -1,
    gaussian_2d,
    borderType=cv2.BORDER_CONSTANT
)

# Size needed for linear convolution in the Fourier domain
h, w = gray_float.shape
kh, kw = gaussian_2d.shape

fft_shape = (h + kh - 1, w + kw - 1)

# Fourier transforms
image_fft_validation = np.fft.fft2(gray_float, fft_shape)
kernel_fft_validation = np.fft.fft2(gaussian_2d, fft_shape)

# Multiplication in frequency domain
full_fourier_result = np.fft.ifft2(
    image_fft_validation * kernel_fft_validation
).real

# Crop result back to original image size
pad_y = kh // 2
pad_x = kw // 2

fourier_equivalent = full_fourier_result[
    pad_y:pad_y + h,
    pad_x:pad_x + w
]

# Calculate numerical difference
difference = np.abs(spatial_equivalent - fourier_equivalent)

mae = np.mean(difference)
max_difference = np.max(difference)

print()
print("VALIDATION RESULTS")
print("------------------")
print("Mean Absolute Difference:", mae)
print("Maximum Difference:", max_difference)

# Save both comparison images
cv2.imwrite(
    "results/spatial_equivalent.jpg",
    np.clip(spatial_equivalent, 0, 255).astype(np.uint8)
)

cv2.imwrite(
    "results/fourier_equivalent.jpg",
    np.clip(fourier_equivalent, 0, 255).astype(np.uint8)
)

print("Validation images saved successfully!")
# ---------------------------------------------------------
# CREATE SIDE-BY-SIDE COMPARISON IMAGE
# ---------------------------------------------------------

# Convert original image to grayscale so all three match
original_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert images to 3-channel BGR for labeling
original_bgr = cv2.cvtColor(original_gray, cv2.COLOR_GRAY2BGR)
spatial_bgr = cv2.cvtColor(
    np.clip(spatial_equivalent, 0, 255).astype(np.uint8),
    cv2.COLOR_GRAY2BGR
)
fourier_bgr = cv2.cvtColor(
    np.clip(fourier_equivalent, 0, 255).astype(np.uint8),
    cv2.COLOR_GRAY2BGR
)

# Add labels
cv2.putText(
    original_bgr,
    "Original",
    (50, 100),
    cv2.FONT_HERSHEY_SIMPLEX,
    2,
    (255, 255, 255),
    4
)

cv2.putText(
    spatial_bgr,
    "Spatial Blur",
    (50, 100),
    cv2.FONT_HERSHEY_SIMPLEX,
    2,
    (255, 255, 255),
    4
)

cv2.putText(
    fourier_bgr,
    "Fourier Blur",
    (50, 100),
    cv2.FONT_HERSHEY_SIMPLEX,
    2,
    (255, 255, 255),
    4
)

# Put all three images next to each other
comparison = np.hstack((original_bgr, spatial_bgr, fourier_bgr))

# Save comparison image
cv2.imwrite("results/comparison.jpg", comparison)

print("Comparison image created successfully!")