import streamlit as st
import base64

st.set_page_config(layout="wide")

def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .overlay {{
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            background-color: rgba(0, 0, 0, 0.5); /* Adjust opacity here */
            z-index: 0;
        }}
        .centered-container {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            z-index: 1;
        }}
        .centered-container h1 {{
            font-size: 4rem;
            font-weight: 700;
            color: white;
            text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.9);
        }}
        .centered-container h3,
        .centered-container h4,
        .centered-container p {{
            color: white;
            text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.8);
        }}
        </style>
        <div class="overlay"></div>
        """,
        unsafe_allow_html=True
    )

set_background("./assets/homepage_bg_image.jpg")  

st.markdown(
    """
    <div class="centered-container">
        <h1>Fashion Analysis</h1>
        <h3><i>Unlock the Style Scoop from Fashion World</i></h3>
        <h4><i>Explore prices, discounts, brands... and many in one place</i></h4>
        <p>With Chatbot support and clean data</p>
    </div>
    """,
    unsafe_allow_html=True
)