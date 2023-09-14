import openai
import os
from dotenv import load_dotenv  

# Set your OpenAI API key environment
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

if "OPENAI_API_KEY" in os.environ:
    openai.api_key = os.getenv("OPENAI_API_KEY")

 
audio_file= open("/Users/rupalivalanju/Documents/Practice/summary/video.mp4", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
converted_text = transcript["text"]
# print(converted_text)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"You are a language model AI developed by OpenAI. Please read the following article and provide a concise summary:\n\n{converted_text}",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

generated_text = response["choices"][0]["text"]

# with open('file.txt', 'w') as f:
#     f.write(generated_text)

# with open('file.txt', 'r') as f:
#     text = f.read() 

print(generated_text)