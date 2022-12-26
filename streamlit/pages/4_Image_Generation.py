import streamlit as st
from transformers import pipeline

# from transformers import AutoTokenizer, AutoModelForTokenClassification

# import torch
# from diffusers import StableDiffusionPipeline
# from diffusers import DiffusionPipeline

print("**Successfully imported diffusers library...")

st.set_page_config(page_title="Image Generation", page_icon="❗")

st.markdown("# Image Generation with Stable Diffusion")
st.sidebar.header("❗ Image Generation - in progress")

st.markdown("This page is in progress... stay tuned!")
# # st.write("We're using a 🤗 model fine-tuned on the English version of the standard CoNLL-2003 Named Entity Recognition dataset.")

# # pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
# pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
# pipe = pipe.to("cuda")

# prompt = "a photo of an astronaut riding a horse on mars"
# st.write(prompt)
# pipe.enable_attention_slicing()
# image = pipe(prompt).images[0]  
# st.write("Successfully generated image")
# st.image(image)

# device = "cuda"
# model_id = "CompVis/ldm-text2im-large-256"

# # load model and scheduler
# ldm = DiffusionPipeline.from_pretrained(model_id)
# ldm = ldm.to(device)

# # run pipeline in inference (sample random noise and denoise)
# prompt = "A painting of a squirrel eating a burger"
# st.write(prompt)
# image = ldm([prompt], num_inference_steps=50, eta=0.3, guidance_scale=6).images[0]

# # save image
# image.save("squirrel.png")

# st.image(image)