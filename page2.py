import streamlit as st
import streamlit as st
import numpy as np
import cv2
from collections import deque
from PIL import Image
import random
import os
from PIL import Image
from moviepy.editor import ImageSequenceClip
import shutil
def main():
    st.title("🌟 Credits and Acknowledgments 🌟")

    st.markdown("""
    ## Special Thanks and Acknowledgments

    I am pleased to present this project, which has been a labor of love and dedication. 

    ### GitHub Profile
    - [**GitHub Profile**](https://github.com/RinkeshKumarSinha)

    ### YouTube Channel
    - [**YouTube Channel**](https://www.youtube.com/channel/UC7dCcEnSsnb9Eyn7Av_uWew) - For Tutorials and insights 

    ### LinkedIn Profile
    - [**LinkedIn Profile**](https://www.linkedin.com/in/rinkesh-kumar-sinha-3a1b0122b/) 

    Thank you for Reviewing the Project Hope You Liked it! 

    <style>
        .stMarkdown {
            text-align: center;
            font-family: 'Arial', sans-serif;
        }
        h1 {
            color: #1f77b4;
        }
        h2 {
            color: #ff7f0e;
        }
        a {
            color: #2ca02c;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
    """, unsafe_allow_html=True)

def app():
    main()
