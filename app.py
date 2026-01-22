import streamlit as st
import requests
import io
from PIL import Image

# --- Page Configuration ---
st.set_page_config(
    page_title="MotoGen | AI Bike Creator",
    page_icon="🏍️",
    layout="centered"
)

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.title("⚙️ Settings")
    st.info("This app uses the Pollinations AI engine to generate bike imagery.")
    aspect_ratio = st.selectbox("Aspect Ratio", ["Square", "Wide", "Tall"])
    enhance_prompt = st.checkbox("Enhance Prompt (adds 'cinematic, 4k')", value=True)

# --- Main UI ---
st.title("🏍️ MotoGen: AI Bike Generator")
st.write("Transform your imagination into high-speed reality.")

prompt = st.text_input("Describe the bike you want to see:", placeholder="e.g. A futuristic neon Ducati in a cyberpunk city")

# Logic for resolution/formatting
width, height = 1024, 1024
if aspect_ratio == "Wide":
    width, height = 1280, 720
elif aspect_ratio == "Tall":
    width, height = 720, 1280

if st.button("Generate Masterpiece"):
    if not prompt.strip():
        st.warning("Please enter a description first!")
    else:
        with st.spinner("🛠️ Engineering your bike..."):
            try:
                # Prompt Engineering
                final_prompt = prompt
                if enhance_prompt:
                    final_prompt += ", hyper-realistic, highly detailed, 8k resolution, cinematic lighting"
                
                # Encode spaces for URL
                encoded_prompt = requests.utils.quote(final_prompt)
                url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&nologo=true"

                response = requests.get(url, timeout=30)
                
                if response.status_code == 200:
                    # Display Image
                    image_bytes = response.content
                    st.image(image_bytes, caption=f"Generated: {prompt}", use_container_width=True)
                    
                    # Download Button
                    st.download_button(
                        label="💾 Download Image",
                        data=image_bytes,
                        file_name="generated_bike.png",
                        mime="image/png"
                    )
                else:
                    st.error("The image engine is currently busy. Please try again in a moment.")
            
            except Exception as e:
                st.error(f"An error occurred: {e}")

st.markdown("---")
st.caption("Powered by Pollinations.ai | Created for Bike Enthusiasts")
