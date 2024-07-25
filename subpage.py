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


def movieMake():
    output_folder = 'output_images'

    # List all .png files in the folder
    image_files = [os.path.join(output_folder, f) for f in sorted(os.listdir(output_folder)) if f.endswith('.png')]

    # Define the output video file
    video_file = 'output_video.mp4'

    # Create the video from the images
    FPPS = st.number_input('Enter the FPS for output video. ', min_value=0, value=4)
    if st.button('Generate Video'):
        clip = ImageSequenceClip(image_files, fps=FPPS)  # Adjust fps as needed
        clip.write_videofile(video_file)

        # Provide a link to download the video
        st.video(video_file)


def is_valid(nrow, ncol, m, n):
    return (nrow >= 0 and ncol >= 0 and nrow < m and ncol < n)

def generate_image(vis, H, W, iteration):
    vis_array = np.array(vis)
    image = np.zeros((H, W, 3), dtype=np.uint8)
    blue = [0, 0, 255]
    green = [25,105,13]

    for i in range(H):
        for j in range(W):
            if vis_array[i, j] == 1:
                image[i, j] = blue
            else:
                image[i, j] = green

    scale_factor = 150
    image_resized = cv2.resize(image, (W * scale_factor, H * scale_factor), interpolation=cv2.INTER_NEAREST)
    return image_resized

def bfs_side_ways(mat, vis, curr_sea_level):
    cnt = 0
    m = len(mat)
    n = len(mat[0])
    q = deque()

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                land_level = mat[i][j]
                if not vis[i][j] and land_level <= curr_sea_level:
                    vis[i][j] = 1
                    cnt += 1
                    q.append((i, j))

    delrow = [-1, 0, 1, 0]
    delcol = [0, 1, 0, -1]

    while q:
        r, c = q.popleft()
        for i in range(4):
            nrow = r + delrow[i]
            ncol = c + delcol[i]

            if is_valid(nrow, ncol, m, n) and not vis[nrow][ncol] and mat[nrow][ncol] <= curr_sea_level:
                q.append((nrow, ncol))
                vis[nrow][ncol] = 1
                cnt += 1
    return m * n - cnt

def generate_random_input():
    H = random.randint(1, 10)
    W = random.randint(1, 10)
    Y = random.randint(1, 15)
    matrix = [[random.randint(1, 100) for _ in range(W)] for _ in range(H)]
    return H, W, Y, matrix

def main():
    st.title('Sinking Land Simulation')

    # Button to generate random input
    if st.button('Generate Random Input'):
        H, W, Y, matrix = generate_random_input()
        matrix_str = '\n'.join(' '.join(map(str, row)) for row in matrix)
        input_data = f"{H} {W} {Y}\n{matrix_str}"
        st.text_area("Matrix and Parameters", value=input_data, height=400)

    # Multi-line text input for matrix and parameters
    input_data = st.text_area("Enter the matrix and parameters Manually or copy and paste from random generated values", 
                              "3 3 5\n10 2 10\n3 1 4\n10 5 10")
    incr = st.number_input('Enter the value by how much sea level increases. each year ', min_value=1, value=1)
    currSea = st.number_input('Enter the value of initial sealevel ', min_value=0, value=1) #note negative sealevel is not allowed
    i=currSea
    year=0

    if st.button('save images and generate video'):
        try:
            # Parse the input data
            lines = input_data.strip().split('\n')
            H, W, Y = map(int, lines[0].split())
            mat = [list(map(int, line.split())) for line in lines[1:]]

            if len(mat) != H or any(len(row) != W for row in mat):
                st.error('Matrix dimensions do not match the input dimensions!')
                return

            vis = [[0] * W for _ in range(H)]
            images = []
            save_folder = 'output_images'
            if os.path.exists(save_folder):
                shutil.rmtree(save_folder)
            os.makedirs(save_folder, exist_ok=True)

           
            while (year<Y + 1):
                curr_sea_level = i
                bfs_side_ways(mat, vis, curr_sea_level)
                image_resized = generate_image(vis, H, W, i)
                images.append(Image.fromarray(image_resized))
                i=i+incr
                year=year+1

                

            st.write(f"Generated {Y} images.")

            for i, img in enumerate(images):
                #st.image(img, caption=f'Iteration {i+1}')

                img_path = os.path.join(save_folder, f'iteration{i}.png')
                img.save(img_path)
        except Exception as e:
            st.error(f"Error: {e}")
    movieMake()

   


def subpage_app():
    main()




