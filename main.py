import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "API_KEY_HERE"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    # Configure Gemini with your Google API key
    genai.configure(api_key="API_KEY_HERE")

    # Create the model (you can use gemini-2.5-flash or gemini-2.5-pro)
    model = genai.GenerativeModel("gemini-2.5-flash")

    # Generate the response
    response = model.generate_content([
        "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud.",
        command
    ])

    # Return the text result
    return response.text

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):  
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apikey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            #Extract the article
            articles = data.get('articles', [])

            # Print the headlines
            for article in articles:
                speak(article['title'])
    # Let OpenAI handles the request
    else:
        # GenAihandles the request
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
        # Listne for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("Recognizing....")
        # recognize speech 
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("Yes")
                # listen for commmand
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:

            print(f"Error: {e}")
