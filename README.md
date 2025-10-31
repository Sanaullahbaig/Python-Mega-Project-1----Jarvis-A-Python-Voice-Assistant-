🎙️ Python Mega Project 3 — JARVIS Virtual Assistant

Jarvis is a Python-based voice assistant that can open websites, play music, fetch live news, and respond intelligently using Google Gemini AI — all through your voice commands! 🧠💬

🚀 Features

✅ Voice-controlled assistant (wake word: “Jarvis”)
✅ Opens popular websites like Google, YouTube, Facebook, Instagram, and LinkedIn
✅ Plays your favorite songs from a custom music library
✅ Reads out the latest news headlines using the News API
✅ Answers general questions using Google Gemini AI
✅ Converts AI responses to speech using gTTS + Pygame

🧩 Requirements

Install all dependencies using:

pip install -r requirements.txt


Your requirements.txt should include:

speechrecognition
pyttsx3
gtts
pygame
requests
google-generativeai

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/your-username/jarvis-voice-assistant.git
cd jarvis-voice-assistant

2️⃣ Create a musicLibrary.py file

This file stores your favorite songs and their links:

# musicLibrary.py
music = {
    "pasoori": "https://www.youtube.com/watch?v=5Eqb_-j3FDA",
    "perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc"
}


You can add or update any songs and use their YouTube URLs.

3️⃣ Add your API keys

Replace this line with your Google API key:

genai.configure(api_key="API_KEY_HERE")


Replace this with your NewsAPI key:

newsapi = "API_KEY_HERE"


🗝️ You can get a free News API key from: https://newsapi.org

🧠 And a Gemini API key from: https://aistudio.google.com/

🧠 How It Works

🎧 Step-by-step process:

The program continuously listens for the wake word “Jarvis”.

Once triggered, it records your next command.

Depending on the command:

It opens websites (e.g., “Open YouTube”)

Plays songs (e.g., “Play Believer”)

Reads top news headlines (e.g., “Tell me the news”)

Or uses Gemini AI to answer questions (e.g., “Who is the Prime Minister of Pakistan?”)

The response is spoken back using Google Text-to-Speech (gTTS).

💬 Example Commands
🗣️ Command	🧠 Action
“Jarvis”	Activates the assistant
“Open Google”	Opens google.com

“Play Perfect”	Plays “Perfect” from your music library
“Tell me the news”	Reads live news headlines
“Who is Allama Iqbal?”	Answers using Gemini AI
⚠️ Notes

Use a stable internet connection for Gemini and News API.

Ensure your microphone is properly configured.

Avoid overlapping voice inputs — wait until Jarvis responds.

🧑‍💻 Author

Sanaullah Mughal
Python Developer 🇵🇰
📧 sanaullahmughal49@gmail.com
