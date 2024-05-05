import chromadb
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from chromadb.utils.data_loaders import ImageLoader
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import streamlit as st
import os

client = chromadb.Client()
embedding_function = OpenCLIPEmbeddingFunction()
image_loader = ImageLoader()

dataset_folder = ".\images"

# --------------------------------------------- Language selection---------------------------------------------------------------

import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

st.title('_TEXT_ :blue[search] 🖼️🔎')
st.markdown('Now search IMAGE using TEXT')
st.divider()

languages = ["Hindi", "Marathi", "Bengali", "Tamil", "Malayalam", "Telugu", "Urdu"]
language_codes = ["hi_IN", "mr_IN", "bn_IN", "ta_IN", "ml_IN", "te_IN", "ur_PK"]

language_mapping = dict(zip(languages, language_codes))


col1, col2 = st.columns([0.7, 0.3])
with col1:
    input = st.text_input("QUERY")

if input is not None:
    
    with col2:

        genre = st.radio(
            "LANGUAGE:",
            ["English", "Another Language"]
        )

        if genre =='Another Language' :
            
            option = st.selectbox(
            "Choose Language:",
            languages)

            selected_language_code = language_mapping[option]

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()  
                
            output = query({
                "inputs": input,
                "parameters": {"src_lang": selected_language_code, "tgt_lang": "en_XX"}
            })

            input = output[0]['translation_text']


#--------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------Text to Text Function -------------------------------------------------------

def main():
                
            collection = client.get_or_create_collection(
            name='multimodal_2', 
            embedding_function=embedding_function, 
            data_loader=image_loader)

            image_uris = sorted([os.path.join(dataset_folder, image_name) for image_name in os.listdir(dataset_folder)])
            ids = [str(i) for i in range(len(image_uris))]

            collection.add(ids=ids, uris=image_uris)

            retrieved = collection.query(query_texts=[input], include=['data'], n_results=10)
            for img in retrieved['data'][0]:
                st.image(img, width=400)

if st.button("submit"):
    if not input:
        st.error('Pls enter the query')
    else:
        main()

#--------------------------------------------------------------------------------------------------------------