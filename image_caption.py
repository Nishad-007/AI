import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()
     

output = query('images/image_4.jpg')
print(output[0]['generated_text'])
# demo = gr.Interface(
#     fn=query,
#     inputs="image",
#     outputs="text",
#     title="Image to Text Converter",
#     description="Upload an image and get the text extracted from it."
# )

# demo.launch()

# image = st.file_uploader("Choose an image file", type=['png', 'jpg', 'jpeg'])

# if st.button("Submit") and image is not None:
#     file_content = image.read()  # Read the content of the uploaded file as bytes
#     file_like_object = io.BytesIO(file_content)  # Create a file-like object
#     output = query(file_like_object)
#     st.write(output)