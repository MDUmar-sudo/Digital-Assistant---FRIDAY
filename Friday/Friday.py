import speech_recognition as sr  # recognise speech
import playsound  # to play an audio file
from gtts import gTTS  # google text to speech
import random
from time import ctime
from datetime import *  # to get time details
import webbrowser  # opens up browser
import time
import os  # for file and apps related functions
import pyautogui  # for screenshots
from bs4 import BeautifulSoup  # for parsing HTMl file
import pyttsx3  # for voice
from requests import get
import requests  # for making requests to browser
from PIL import Image
from playsound import playsound
import wikipedia
import jokes  # custom module for jokes
import mails  # custom module for sending mails
import DOB  # custom module for assistant age
import fun_facts  # custom module for fun facts
import WhatsApp  # custom module for sending whatsapp messages
import Weather_API as wthr  # custom module for getting weather information
import News_API as nws  # custom module for getting latest news


# SpeechRecognition module uses pyaudio module implicitly


class person:
    name = ''

    def setName(self, name):
        self.name = name


class asis:
    name = ''

    def setName(self, name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


def engine_speak(text, voices=None):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # index 0 for male voice and 1 for female voice
    engine.setProperty('rate', 170)  # controls wpm (default='200 wpm')
    text = str(text)
    engine.say(text.lower())
    print("<<", text)
    engine.runAndWait()


r = sr.Recognizer()  # initialize a recogniser ( listen for audio and convert it to text)


def record_audio(ask=""):
    with sr.Microphone() as source:  # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, timeout=5, phrase_time_limit=4)  # listen for the audio via source
        r.adjust_for_ambient_noise(source)

        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)  # covert audio to text
        except sr.UnknownValueError:  # error: recognizer doesn't understand
            engine_speak("Sorry,I could not get that")

        except sr.RequestError:
            engine_speak(
                "Sorry,You're system in not connected to data.So cannot help you at the moment")  # error:recognizer is not connected
        print(">>", voice_data.lower())  # print what user said
        return voice_data.lower()


#  get string and make a audio file to be played

def engine_audio(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en-in')
    r = random.randint(1, 2000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    print(asis_obj.name + ":", audio_string)  # print what app said
    os.remove(audio_file)  # remove audio file


def respond(voice_data):
    # 1: greeting
    if there_exists(['hey', 'hi', 'hello', "what's up"]) and "in" not in voice_data:
        greetings = ["hey,how can I help you " + person_obj.name, "hey,what's up? " + person_obj.name,
                     "I'm listening " + person_obj.name, "how can I help you? " + person_obj.name]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        engine_speak(greet)

    # 2: name
    if there_exists(["what is your name", "what's your name"]):  # assistance name

        if person_obj.name:
            engine_speak(f"My name is {asis_obj.name},{person_obj.name}")  # gets users name from voice input
        else:
            engine_speak(f"My name is {asis_obj.name}.what's your name?")  # in case you haven't provided your name

    if there_exists(["my name"]):  # user name
        engine_speak("Your name is " + person_obj.name)

    # 3: knowing well being
    if there_exists(["how are you"]):
        engine_speak("I'm very well, thanks for asking sir. how are you?")

    if there_exists(["i am fine", "i am very well"]):
        engine_speak("glad to here that")

    # 4: time
    if there_exists(["what time is it", "tell me the time", "what's the time", "what is the time"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and  " + minutes + " minutes"
        engine_speak(time)

    # 5: search google
    if there_exists(["search google for", "open google and search for", "search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("here what I have found on the web for you sir on" + search_term)

    # 6:search youtube
    if there_exists(["search youtube for", "open youtube and search for"]):
        search_term = voice_data.split('for')[-1]
        search_term = search_term.replace("on youtube", "").replace("search", "")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I have found on youtube on " + search_term)

    # 7: get stock price
    if there_exists(["price of stock market", "stock price", "stock market"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("here, is what I have found on the web" + search_term)

    # 8: opening notepad
    if there_exists(["open notepad", "notepad"]):
        os.system("start Notepad")
        engine_speak("Opening notepad")

    # 9: weather
    if there_exists(["weather", "weather report", "weather in", "temperature in delhi", "temperature"]):
        search_term = voice_data.split("in")[-1]
        temp, time, sky = wthr.getWeather(search_term)
        engine_speak(f"current temperature in {search_term} is " + temp)
        engine_speak(f"It's {time} and while sky has {sky}")

    # 10: stone paper scissors
    if there_exists(["game", "Let's play a game"]):
        engine_speak("Let's play rock paper scissor")
        voice_data = record_audio("choose among rock, paper, scissor")
        flag = 0
        moves = ["rock", "paper", "scissor"]

        pmove = voice_data
        print(pmove)

        cmove = random.choice(moves)
        engine_speak(cmove)

        if pmove == cmove:
            engine_speak("the match is draw")
        elif pmove == "rock" and cmove == "scissor":
            flag = 1
            engine_speak("you won sir")
        elif pmove == "paper" and cmove == "scissor":
            flag = 1
            engine_speak("I won sir")
        elif pmove == "scissor" and cmove == "rock":
            flag = 1
            engine_speak("I won sir")
        elif pmove == "paper" and cmove == "rock":
            flag = 1
            engine_speak("you won sir")
        elif pmove == "rock" and cmove == "paper":
            flag = 1
            engine_speak("I won sir")
        elif pmove == "scissor" and cmove == "rock":
            flag = 1
            engine_speak("I won sir")
        elif pmove == "scissor" and cmove == "paper":
            flag = 1
            engine_speak("I won sir")

        if flag == 1:
            playsound(r"C:\Users\Assassin\Desktop\py_hub\Assistant_Friday\audio_file\applause.mp3")

    # 11: toss a coin
    if there_exists(["toss", "flip"]):
        moves = ["head", "tail"]
        cmove = random.choice(moves)
        playsound(r"C:\Users\Assassin\Desktop\py_hub\Assistant_Friday\audio_file\Coin Toss.mp3")
        engine_speak("its a " + cmove)

    # 12: clalulator
    if there_exists(["plus", "minus", "multiply", "divide", "power", "+", "-", "*", "/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            a = int(voice_data.split()[0]) + int(voice_data.split()[2])
            engine_speak(f"Answer is {a}")
        elif opr == '-':
            a = int(voice_data.split()[0]) - int(voice_data.split()[2])
            engine_speak(f"Answer is {a}")
        elif opr == 'multiply':
            a = int(voice_data.split()[0]) * int(voice_data.split()[2])
            engine_speak(f"Answer is {a}")
        elif opr == 'divide':
            a = int(voice_data.split()[2]) / int(voice_data.split()[0])
            engine_speak(f"Answer is {a}")
        elif opr == 'power':
            a = int(voice_data.split()[0]) ** int(voice_data.split()[2])
            engine_speak(f"Answer is {a}")
        else:
            engine_speak("Wrong Operator")

    # 12:screenshot
    if there_exists(["capture", "my screen", "screenshot", ]):
        try:
            myScreenshot = pyautogui.screenshot()
            f = random.randint(1, 100000)
            myScreenshot.save(f"C:\\Users\\Assassin\\Pictures\\Screenshots\\capture_{f}.jpg")
            engine_speak("I have taken a screen shot")
            engine_speak("here have a look")
            filename = f"C:\\Users\\Assassin\\Pictures\\Screenshots\\capture_{f}.jpg"
            img = Image.open(filename)
            img.show()
        except Exception as e:
            engine_speak("sorry I m unable to process your request")

    # 13: current location in google maps
    if there_exists(["what's my location", "where am i", "tell me my location", "what is my location"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("You must be somewhere near here, as per Google maps")

    # 14: thanking assistant
    if there_exists(["thanks", "thank", "you are helpful", "very helpful"]):
        response = ["It's my job to help you sir", "No need to mention sir", "you are always welcome sir",
                    "I am always here to help", "you are very kind to say that"]
        rp = random.choice(response)
        engine_speak(rp)
        engine_speak("Is there anything else sir?")
    # 15: roll a dice
    if there_exists(["roll a dice", "throw a dice", "dice"]):
        outcome = random.randint(1, 6)
        playsound(r"C:\Users\Assassin\Desktop\py_hub\Assistant_Friday\audio_file\Dice Roll.mp3")
        engine_speak("It's a " + str(outcome))

    # 16:open cmd
    if there_exists(["open cmd", "command prompt"]):
        os.system('start cmd')
        engine_speak("opening command prompt")

    # 17:to find location
    if there_exists(["open google maps and search the location of", "find location of", "what is the location of",
                     "location of"]):
        location = voice_data.split("of")[-1]
        url = 'https://www.google.nl/maps/place/search?q=' + location + '/&amp'
        webbrowser.get().open(url)
        engine_speak("here is the location of" + location)

    # 18:opening photoshop
    if there_exists(["open photoshop"]):
        os.system('start Photoshop')
        engine_speak("opening adobe photoshop")

    # 19:to play music
    if there_exists(["play music", "play songs", "play song", "play a song"]):
        music_dir = r"C:\Users\Assassin\Desktop\py_hub\Assistant_Friday\Music"
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        os.startfile(os.path.join(music_dir, rd))

    # 20: getting ip address
    if there_exists(["get my ip address", "what is my ip address", "ip address"]):
        ip = get("https://api.ipify.org?format=json").text
        engine_speak("your IP address is" + ip)

    # 21: definitions from wikipedia
    if there_exists(["wikipedia search", "search wikipedia"]):
        engine_speak("searching wikipedia...")
        wiki = voice_data.replace("wikipedia", "")
        wi_text = wikipedia.summary(wiki, sentences=2)
        engine_speak("according to wikipedia")
        engine_speak(wi_text)

    # 22: sending message on whatsapp
    if there_exists(["send message to"]):
        data = voice_data.split("to")[-1]
        number = WhatsApp.recipient(data)
        engine_speak("what should i send")
        content = record_audio().lower()
        try:
            WhatsApp.message(number, content)
            engine_speak("message has been sent")
        except Exception as e:
            print(e)
            engine_speak("Sorry unable to send the message")

    # 23: who created you
    if there_exists(["who created you"]):
        engine_speak(f"Sir,i am a brain child of {person_obj.name}.")

    # 24: time of creation
    if there_exists(["how old are you"]):
        age = DOB.dob(date(2021, 7, 11))
        engine_speak("Ahhhhh. well sir, you should never ask a women her age.")
        engine_speak(f"By the way,I'm {age} old")

    # 25: you are amazing
    if there_exists(["you are amazing", "you are great"]):
        engine_speak("it's so nice of you to say that. thank you")

    # 26: jokes
    if there_exists(["tell me a joke", "joke"]):
        joke = jokes.myjokes()
        engine_speak(joke)

    # 27: fun facts
    if there_exists(["tell me fun facts", "interesting facts"]):
        fact = fun_facts.facts()
        engine_speak("Do you know? " + fact)

    # 28: acronym for friday
    if there_exists(["meaning of your name"]):
        engine_speak(
            "Actually sir, my name friday is acronym for Female Replacement Intelligent Digital Assistant Youth")

    # 29: sending mails
    if there_exists(["send mail to", "send a mail to"]):
        data = voice_data.split("to")[-1]
        to = mails.recipient(data)
        engine_speak("what should i write in mail")
        content = record_audio().lower()
        try:
            mails.sendEmail(to, content)
            engine_speak("email has been sent")
        except Exception as e:
            print(e)
            engine_speak("Sorry unable to send the mail")

    # 31: taking notes
    if there_exists(["take a note"]):
        try:
            engine_speak("what should I write down?")
            note = record_audio().lower()
            n = random.randint(1, 100)
            f = open(f"C:\\Users\\Assassin\\Desktop\\py_hub\\Assistant_Friday\\notes\\note{n}.txt", 'w')
            f.write(note)
            f.close()
            engine_speak("I have noted that down sir")
        except Exception as e:
            engine_speak("Sorry sir, I'm unable to take a note at the moment")

    #  33: getting news
    if there_exists(["news of the day", "tell me news"]):
        news = nws.getNews()
        for i in range(len(news)):
            engine_speak(news[i])

    # 32:end
    if there_exists(["bye", "log out", "goodbye", "no", "good night"]):
        engine_speak("goodbye. Thanks for using me sir. Have a nice day")
        exit()


def greet():
    hour = int(datetime.now().hour)
    if 0 < hour and hour < 12:
        engine_speak("good morning")
    elif 12 <= hour and hour <= 16:
        engine_speak("good afternoon")
    else:
        engine_speak("good evening")
    engine_speak(f"I am {asis_obj.name}")
    city = "delhi"
    temp, time, sky = wthr.getWeather(city)
    engine_speak(f"currently it's {time} and temperature in {city} is {temp}. while sky has {sky}.")
    engine_speak("Tell me how may i assist you today sir.")


time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = "Friday"
person_obj.name = "MD"

# playsound(r"C:\Users\Assassin\Desktop\py_hub\Assistant_Friday\audio_file\F.R.I.D.A.Y.mp3")
greet()
while True:
    print("listening...")
    voice_data = record_audio("")  # get the voice input
    respond(voice_data)  # respond
