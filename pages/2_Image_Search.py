import chromadb
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from chromadb.utils.data_loaders import ImageLoader
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import os
import streamlit as st 

client = chromadb.Client()
embedding_function = OpenCLIPEmbeddingFunction()
image_loader = ImageLoader()

dataset_folder = ".\images"

st.title('_IMAGE_ :blue[search] 🖼️🔎')
st.markdown('Now search IMAGE using IMAGE')
st.divider()

col1, col2 = st.columns([0.7, 0.3])

with col1:
    file_uploader = st.file_uploader("Upload and Image(JPG or PNG)")

with col2:
    if file_uploader:
        st.write("Uploaded Image")
        st.image(file_uploader, width=400)

def ii():

    collection = client.get_or_create_collection(
        name='multimodal_collection', 
        embedding_function=embedding_function, 
        data_loader=image_loader)

    image_uris = sorted([os.path.join(dataset_folder, image_name) for image_name in os.listdir(dataset_folder)])
    ids = [str(i) for i in range(len(image_uris))]

    collection.add(ids=ids, uris=image_uris)

    query_image = np.array(Image.open(file_uploader))
    
    
    # st.image(query_image)
    # print("Query Image")
    # plt.imshow(query_image)
    # plt.axis('off')
    # plt.show()

    
    retrieved = collection.query(query_images=[query_image], include=['data'], n_results=3)
    st.write("Similar Images")
    for img in retrieved['data'][0][1:]:
        # print(retrieved['data'])
        # print(image_uris)
        # print(f'data: {img}')
        # plt.imshow(img)
        st.image(img, width=400 )
        plt.axis("off")
        plt.show()
    

if st.button('submit'):
    ii()
