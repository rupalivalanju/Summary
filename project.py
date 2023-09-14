# import openai
# import os
# from dotenv import load_dotenv  
# import streamlit as st

# # Set your OpenAI API key environment
# load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

# if "OPENAI_API_KEY" in os.environ:
#     openai.api_key = os.getenv("OPENAI_API_KEY")


# ÷def convert_audio_to_text(uploaded_audio):
#     # Read the audio file as binary data
#     audio_data = uploaded_audio.read()
import openai
import io
import os
from dotenv import load_dotenv  
import streamlit as st

# Set your OpenAI API key environment
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

if "OPENAI_API_KEY" in os.environ:
    openai.api_key = os.getenv("OPENAI_API_KEY")

def convert_audio_to_text(uploaded_audio):
    # Read the audio file as binary data
    audio_data = uploaded_audio.read()

    # Create a BytesIO object with the audio data and a name attribute
    audio_file = io.BytesIO(audio_data)
    audio_file.name = uploaded_audio.name  # Set the name attribute

    # Call the OpenAI API with the Whisper ASR system
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    return transcript["text"]
 
def main():
    st.title("Audio to Text Transcription")

    uploaded_file = st.file_uploader("Upload an audio file (MP3/WAV)", type=["mp3", "wav","mp4"])

    if uploaded_file:
        st.audio(uploaded_file, format="audio/mp3")

        text_output = convert_audio_to_text(uploaded_file)
        st.header("Converted Text:")
        st.write(text_output)

if __name__ == "__main__":
    main()

