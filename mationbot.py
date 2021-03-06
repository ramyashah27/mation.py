import pyttsx3 
import speech_recognition as sr 
import os
import pyjokes
import random
import wikipedia
import weather_forecast as wf
from playsound import playsound
import datetime
import time
import cv2
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

clock= time.ctime()
aweatherfor=wf.forecast(place = "ahmedabad" , time="23:15:00" , date="2021-01-09" , forecast="daily")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am MATION Sir. Please tell me how may I help you")       

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'discord' in query:
            print('opening discord for YOU')
            speak('opening discord for YOU')
            codepath= 'C:\\Users\\ADMIN\\Desktop\\ramya shah\\Discord.lnk'
            os.startfile(codepath)
        if "zoom" in query:
            print("opening ZOOM")
            speak("opening ZOOM")
            codepathzoom="C:\\Users\\ADMIN\\Desktop\\des\\zoom.lnk"
        
            os.startfile(codepathzoom)
        elif "html" in query:
            print("wait")
        if "weather" in query:
            print(aweatherfor)
            speak(aweatherfor)
        if "joke" in query:
            cjoke=pyjokes.get_joke()
            print(cjoke)
            speak(cjoke)
        if "time" in query:
            aclock=time.ctime()
            print(aclock)
            speak(aclock)
        if "camera" in query:
            cam = cv2.VideoCapture(0)
            while cam.isOpened():
                ret, frame = cam.read() 
                if cv2.waitKey(10) == ord('q'):
                    break
                cv2.imshow('ramya shah', frame)
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        if "music" in query:
            speak('NOW PLAYING dheeme dheeme FOR you')
            playsound('C:\\Users\\ADMIN\\Desktop\\python\\chapter 1\\Dheeme Dheeme.mp3')
        if "google" in query:
            speak("opening google for u")
            webbrowser.open('https://www.google.com/')    
        elif "youtube" in query:
            speak("OPENING YOTUBE FOR YOU")
            webbrowser.open("https://www.youtube.com/")
        elif "github" in query:
            speak('github is OP opening it--> ')
            print('-->')
            webbrowser.open("https://www.github.com")
        # if "hello" or "hi" in query:
        #     speak("NAMASTE")
        #     print("hello sir how are u?")
        #     speak("hello SIR how are u?")
      
        if "remind me" in query:
            print("what u want to remind me")
            speak("what u want to remind me")    
            rocker= takeCommand()
            fft = (f"\n at ({clock}) YOU TOLD TO REMIND ME: -->  {rocker}")
            fft = str(fft)

            with open("remindeer.txt", "w") as wrf:
                wrf.write(fft)
                print(f"reminder set: {rocker}")
            with open("remindeerapp.txt", "a") as wrfapp: 
                wrfapp.write(fft)
            speak("reminder set for today")
        if "what are my reminders" in query:
            with open("remindeer.txt") as remf:
                reqre=remf.read()
                speak(f"u told to remind me {reqre}")
                print(f" :   {reqre}")
        if query=="stop":
            speak("bbye sir thanks for using me")
            print("bbye sir thanks for using me")
            break