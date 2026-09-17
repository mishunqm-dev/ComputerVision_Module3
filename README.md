# CSC 8830 - Module 3: Image Blurring

## Project Overview

This project demonstrates image blurring using two approaches:

1. Spatial-domain filtering
2. Fourier-domain filtering

The purpose of the project is to demonstrate the convolution theorem:

Convolution in the spatial domain is equivalent to multiplication in the frequency domain.

## Spatial-Domain Filtering

A Gaussian filter is applied directly to the image using convolution.

## Fourier-Domain Filtering

The image and Gaussian filter are transformed into the frequency domain using the Fourier Transform.

The transformed image and filter are multiplied together, and the inverse Fourier Transform is used to return the result to the spatial domain.

## Validation

The two filtering approaches were compared numerically.

Mean Absolute Difference:

0.00000305

Maximum Difference:

0.00001457

These extremely small differences demonstrate that the two approaches produce essentially the same result.

## Files

- `blur_compare.py` - performs spatial and Fourier-domain filtering
- `app.py` - Streamlit web application
- `requirements.txt` - required Python packages
- `test_images/` - input image
- `results/` - generated output images

## Run the Image Processing Script

```bash
python3 blur_compare.py