from argparse import Action
from json.tool import main
from winreg import HKEY_LOCAL_MACHINE
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser 
import webbrowser as web
import os
import smtplib
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
from keyboard import press
from keyboard import press_and_release
from numpy import true_divide



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


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
           
        print("Say that again please...")  
        return "None"
    return query



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello my Friend i am Budddy. your personal assistant. Please tell me how may I help you")       






def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('himanshupatil1111@gmail.com', 'VEDANTfrto@119')
    server.sendmail('himanshupatil1111@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    
    
    wishMe()
    while True:
    
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube search' in query:
            from features import youtubesearch
            youtubesearch(query)

        elif 'google' in query:
            from features import googlesearch
            googlesearch(query)

        elif 'where is' in query:
            from features import GoogleMaps

            
            Place = query.replace("where is ","")
            
            GoogleMaps(Place)

            

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'youtube' in query:
            from features import youtubeauto
            youtubeauto(query)

        elif 'movie time' in query:
            webbrowser.open("netflix.com")

        elif 'open zoom' in query:
            webbrowser.open("zoom.com") 

        elif 'open geekforgeek' in query:
            webbrowser.open("geekforgeek.com")  

        elif 'check speed of internet' in query:
            webbrowser.open("fast.com")  

        elif 'my location' in query:
            from features import My_Location

        elif 'quit' in query:
            break

            

            My_Location()


        elif 'play music' in query:
            music_dir = 'C:\\Users\\Babita Majumdar\\Downloads\\Sixth semester\\BuddyPA\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play favourite song' in query:
            music_dir = 'C:\\Users\\Babita Majumdar\\Downloads\\Sixth semester\\BuddyPA\\loved music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'tell me time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        

        elif 'email my friend' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kunalkhadse1555@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Himanshu. I am not able to send this email")   