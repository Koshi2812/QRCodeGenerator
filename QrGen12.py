import streamlit as st
import qrcode
from PIL import Image
import io
import base64

# ✅ Set page configuration
st.set_page_config(page_title="📍 Google Maps QR Code Generator", layout="centered")

# ✅ Function to add background image from local file
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ Call the background image function (change to your image file name)
add_bg_from_local("qrimage.jpg")  # or "qrcode.png" or any image you have in the same folder

# ✅ App title and input
st.title("📍 Google Maps QR Code Generator")
url = st.text_input("Enter Google Maps URL (or any URL):")

# ✅ Generate QR code on button click
if st.button("Generate QR Code"):
    if url.strip() == "":
        st.warning("⚠ Please enter a valid URL.")
    else:
        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert to BytesIO
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Show image and download
        st.image(buffer, caption="Your QR Code", use_container_width=True)
        st.success("✅ QR Code generated successfully!")

        st.download_button(
            label="📥 Download QR Code",
            data=buffer,
            file_name="qr_code.png",
            mime="image/png"
        )
