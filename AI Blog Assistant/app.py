import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key 

# Ensure API keys are retrieved from environment variables for security
genai.configure(api_key=google_gemini_api_key)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

#set page to wide mode
st.set_page_config(layout="wide")

#title of app
st.title('BlogBotAI : Your AI Writing Companion')

# create a subheader
st.subheader("Now you can craft perfect blogs with the help of AI. BlogBotAI is your new AI Blog Comapanion")

# sidebar for user input
with st.sidebar:
    st.title("Input Your Blog Details")
    st.subheader("Enter Details of the Blog you want to generate")

    # blog title
    blog_title=st.text_input("Blog Title")

    # keywords input
    keywords=st.text_area("Keywords (comma-separated)")

    #Number of words
    num_words = st.slider("Number of words", min_value=250, max_value=1000, step=250)

    # number of images
    # num_images = st.number_input("Number of images", min_value=1, max_value=5, step=1)

    # Submit button
    submit_button = st.button("Generate Blog")

if submit_button:
    
    # Generate blog content
    prompt = f'Generate a comprehensive, engaging blog post relevant to the given title "{blog_title}" and keywords "{keywords}". The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout.'
    chat_session = model.start_chat(
        history=[
            {"role": "user", "parts": [prompt]},
        ]
    )

    response = chat_session.send_message(prompt)

    #st.title("YOUR BLOG POST:")

    st.write(response.text)
