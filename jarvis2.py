import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio

engine = pyttsx3.init()

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[33].id)

def speak(audio):

    engine.say(audio) 
    
    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour in range(5,13):
        speak("Good Morning boss")
    elif hour in range(13,17):
        speak("Good Afternoon boss")
    elif hour in range(17,22):
        speak("Good Evening boss")
    elif hour in range(22,24) or hour in range(0,6):
        speak("Night is young boss")

    speak("How may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f'user said{query}\n')

    except Exception as e:
        print('Sorry, say that again please')
        return "none"
    return query

 


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)