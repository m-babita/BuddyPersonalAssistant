from argparse import Action
from json.tool import main
from winreg import HKEY_LOCAL_MACHINE
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser 
import webbrowser as web
import pywhatkit
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
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def youtubesearch(term):
    result="https://www.youtube.com/results?search_query=" + term
    web.open(result)
    speak("here what i found")
    pywhatkit.playonyt(term)
    speak("this may help you")

def googlesearch(what):
    result="https://www.google.co.in/search?q=" + what
    web.open(result)
    speak("here what i found")

def GoogleMaps(Place):

    Url_Place = "https://www.google.com/maps/place/" + str(Place)

    geolocator = Nominatim(user_agent="myGeocoder")

    location = geolocator.geocode(Place , addressdetails= True)

    target_latlon = location.latitude , location.longitude

    web.open(url=Url_Place)

    location = location.raw['address']

    target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}

    current_loca = geocoder.ip('me')

    current_latlon = current_loca.latlng

    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)


    speak(target)
    speak(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ")

def My_Location():

    op = "https://www.google.com/maps/place/Delhi/@28.6472799,76.8130619,83757m/data=!3m2!1e3!4b1!4m5!3m4!1s0x390cfd5b347eb62d:0x37205b715389640!8m2!3d28.7040592!4d77.1024902"

    speak("Checking....")

    web.open(op)

    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    speak(f"Sir , You Are Now In {state , country} .")


def youtubeauto(command):
    query=str(command)

    if "pause" in query:
        press('k')

    elif "resume" in query:
        press('k')

    elif "full screen" in query:
        press('f')

    elif "skip" in query:
        press('l')
    
    elif "mute" in query:
        press('m')
    
    elif "unmute" in query:
        press('m')

    elif "back" in query:
        press('j')
    
    elif "speed up" in query:
        press_and_release('shift+>')

    elif "slow down" in query:
        press_and_release('shift+<')

    elif "next video" in query:
        press_and_release('shift+n')

    elif "previous video" in query:
        press_and_release('shift+p')

