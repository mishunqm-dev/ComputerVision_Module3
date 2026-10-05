# Image Blurring: Spatial & Fourier Domain Filtering

This project uses Python and OpenCV to explore image blurring through spatial-domain convolution and Fourier-domain filtering. The project demonstrates the convolution theorem by implementing Gaussian filtering using both approaches and comparing the resulting images numerically.

An interactive Streamlit application is also included for presenting and exploring the image-processing results.

## Technologies Used

- Python
- OpenCV
- NumPy
- Streamlit
- Image Processing
- Gaussian Filtering
- Fourier Transform
- Spatial-Domain Convolution

## Project Overview

This project demonstrates image blurring using two approaches:

1. Spatial-domain filtering
2. Fourier-domain filtering

The primary objective is to demonstrate the convolution theorem:

> Convolution in the spatial domain is equivalent to multiplication in the frequency domain.

The outputs from both approaches are compared numerically to verify that they produce nearly identical results.

## Spatial-Domain Filtering

A Gaussian filter is applied directly to the image using convolution.

This approach performs the filtering operation directly on the image pixels in the spatial domain.

## Fourier-Domain Filtering

The image and Gaussian filter are transformed into the frequency domain using the Fourier Transform.

The transformed image and filter are multiplied together, and the inverse Fourier Transform is then used to return the result to the spatial domain.

This demonstrates the relationship between spatial-domain convolution and frequency-domain multiplication.

## Validation

The two filtering approaches were compared numerically.

**Mean Absolute Difference:**

`0.00000305`

The extremely small difference demonstrates that the spatial-domain and Fourier-domain implementations produce nearly equivalent results.

## Project Files

- `blur_compare.py` - performs spatial-domain and Fourier-domain image blurring and compares the results
- `app.py` - Streamlit application for displaying and exploring the image-processing results
- `requirements.txt` - Python dependencies required to run the project
- `test_images/` - source images used for testing
- `results/` - generated image-blurring results
- `.gitignore` - excludes unnecessary files from version control

## Run the Project

Install the required dependencies:

```bash
python3 -m pip install -r requirements.txt
