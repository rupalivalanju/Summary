# Summary bot


## Video Summarization using Whisper AI 

1. Introduction
The "Video Summarization using Whisper AI" project aims to demonstrate the process of transcribing audio from videos and extracting text summaries using the OpenAI Whisper ASR (Automatic Speech Recognition) system. The application allows users to upload video files (in MP3, WAV, or MP4 formats), transcribe the audio content, and display the extracted text summarization.

2. Objective
The objective of this project is to showcase the capabilities of the OpenAI Whisper ASR system in transcribing audio content from videos and generating text summaries. By leveraging the Whisper ASR API, users can extract meaningful insights from video content and create concise summaries.

3. Technologies Used
• OpenAI API: To access the Whisper ASR system for audio transcription.
• Streamlit: A Python library for creating interactive web applications with minimal effort.
• Python: The programming language used to develop the application.
• io, os, dotenv: Standard Python modules for handling file I/O, environment variables, and data streaming.

4. Code Overview
The code provided demonstrates the integration of the OpenAI Whisper ASR system with a Streamlit web application. The application allows users to upload audio/video files, transcribe the audio using Whisper ASR, and display the extracted text summarization.
The main components of the code include:
• Setting up OpenAI API key from environment variables using dotenv.
• Defining a function convert_audio_to_text to transcribe audio from uploaded files using Whisper ASR.
• Using Streamlit to create a simple web interface for uploading audio/video files and displaying results.


5. Running the Application
To run the application, follow these steps:
• Set up your OpenAI API key in a .env file.
• Install the required Python packages using pip install openai io streamlit python-dotenv.
• Execute the provided code in a Python environment.
• The Streamlit app will be launched in your browser.
• Upload an audio/video file (MP3, WAV, MP4) and click the "Submit" button.
• The audio will be transcribed using the Whisper ASR system, and the extracted textsummarization will be displayed.


7. Conclusion
The "Video Summarization using Whisper AI" project demonstrates the potential of the OpenAI Whisper ASR system in extracting valuable information from video content. By integrating this ASR system with a Streamlit application, users can easily transcribe audio content and generate text summaries, contributing to various applications such as video analysis, content indexing, and more.
