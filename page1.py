import streamlit as st
from subpage import subpage_app
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
def app():
    st.title("Instructions")
    st.markdown("""
    ## Simulates what ?

    There is an island of size H×W, surrounded by the sea. 

    The island is divided into H rows and W columns of 1×1 sections, and the elevation of the section at the i-th row from the top and the j-th column from the left (relative to the current sea level) is 
    Ai,j​.

    Starting from now, the sea level rises by 1 each year.
                
    Here, a section that is vertically or horizontally adjacent to the sea or a section sunk into the sea and has an elevation not greater than the sea level will sink into the sea.
                
    Here, when a section newly sinks into the sea, any vertically or horizontally adjacent section with an elevation not greater than the sea level will also sink into the sea simultaneously, and this process repeats for the newly sunk sections.
    
                
    For each i=1,2,…,Y, find the area of the island that remains above sea level i years from now.
    
    ## How the input should be given
                
    H W Y
    next takes H X W dimension matrix 
    You can do further adjustments to generate the desired simulation.

    <style>
        .stMarkdown {
            text-align: left;
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
    st.write("Don't try to pick a larger Y as the system cannot handle large picture generation. ")

    # Load the subpage
    subpage_app()