# PROJECT 16: TRIPLE GLORY 333-BYTE VOICE ASSISTANT
# Author: Chukwugloryuchechi333-byte
# From Ebonyi to NVIDIA

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Setup voice
engine = pyttsx3.init()
engine.setProperty('rate', 160) # Speed of talk

def speak(text):
    print(f"Glory AI: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Talk now!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            command = r.recognizer.recognize_google(audio, language='en-NG')
            print(f"You said: {command}")
            return command.lower()
        except:
            # If no mic / for phone users - use text
            print("No mic detected, using text mode")
            command = input("Type your command: ")
            return command.lower()

def run_assistant():
    speak("Hello! I am Triple Glory 333 Byte Voice Assistant. How can I help you?")
    
    while True:
        query = listen()
        
        if "time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")
            
        elif "your name" in query:
            speak("I am Triple Glory 333 Byte, created by Chukwu Glory Uchechi")
            
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")
            
        elif "how are you" in query:
            speak("I am fine, Triple Glory is shining!")
            
        elif "stop" in query or "bye" in query or "exit" in query:
            speak("Goodbye Glory! See you tomorrow for Project 17!")
            break
            
        else:
            speak("I heard you say " + query + ". I am still learning!")

# START
if __name__ == "__main__":
    run_assistant()
