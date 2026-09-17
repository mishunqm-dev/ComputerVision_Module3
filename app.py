import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Module 3 - Image Blurring",
    layout="wide"
)

st.title("CSC 8830 - Module 3: Image Blurring")

st.write("""
This project demonstrates image blurring using both spatial-domain
filtering and Fourier-domain filtering.

The goal is to show that convolution in the spatial domain is equivalent
to multiplication in the frequency domain.
""")

st.header("Original Image")

original = Image.open("test_images/Plant.jpeg")
st.image(original, caption="Original Image", use_container_width=True)

st.header("Spatial Domain Filtering")

st.write("""
A Gaussian filter was applied directly to the image in the spatial domain.
This process performs convolution between the image and the Gaussian kernel.
""")

spatial = Image.open("results/spatial_equivalent.jpg")
st.image(spatial, caption="Spatial Domain Blur", use_container_width=True)

st.header("Fourier Domain Filtering")

st.write("""
The same Gaussian filter was transformed into the frequency domain.
The Fourier transform of the image was multiplied by the Fourier transform
of the filter, and then the inverse Fourier transform was used to return
the result to the spatial domain.
""")

fourier = Image.open("results/fourier_equivalent.jpg")
st.image(fourier, caption="Fourier Domain Blur", use_container_width=True)

st.header("Side-by-Side Comparison")

comparison = Image.open("results/comparison.jpg")
st.image(
    comparison,
    caption="Original | Spatial Blur | Fourier Blur",
    use_container_width=True
)

st.header("Validation Results")

st.metric(
    "Mean Absolute Difference",
    "0.00000305"
)

st.metric(
    "Maximum Difference",
    "0.00001457"
)

st.success("""
The extremely small numerical differences show that spatial-domain
convolution and frequency-domain multiplication produced essentially
the same result.
""")

st.header("Theory")

st.latex(r"g(x,y) = f(x,y) * h(x,y)")

st.write("Spatial-domain convolution")

st.latex(r"G(u,v) = F(u,v)H(u,v)")

st.write("Frequency-domain multiplication")

st.write("""
This demonstrates the convolution theorem:

Convolution in the spatial domain is equivalent to multiplication
in the Fourier domain.
""") 