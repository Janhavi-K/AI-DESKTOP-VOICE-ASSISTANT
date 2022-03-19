import pyttsx3                                                  # text to speech converter
import datetime                                                 # supplies classes for manipulating date and time
import speech_recognition as sr                                 # speech recognizer                   
import wikipedia                                                # accesses and parses data from Wikipedia
import webbrowser                                               # provides a interface to allow displaying Web-based documents to users                                               
import os                                                       # provides functions for interacting with the operating system    
import requests                                                 # allows you to send HTTP requests using Python
import random                                                   # use to make random numbers
import pyjokes                                                  # jokes
import operator                                                 # exports a set of efficient functions 
import pyautogui                                                # used to programmatically control the mouse & keyboard
import time
import re                                                       # provides regular expression matching operations
import sqlite3                                                  # to read query and write SQL databases from Python
import list_of_installed_apps
from bs4 import BeautifulSoup                                   # pulls the data out of HTML and XML files
import cv2
import ctypes                                                   # provides C compatible data types, and allows calling functions in DLLs or shared libraries
import psutil                                                   # Process and system utilities(CPU, memory, disks, network, sensors)
import speedtest


engine = pyttsx3.init('sapi5')                                  # init function to get an engine instance for the speech synthesis
voices = engine.getProperty('voices')                           # gets current value of engine property
print(voices[0].id)                                             
engine.setProperty('voice',voices[0].id)                        # Queues a command to set an engine property.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()                                         # Blocks while processing all currently queued commands.

def wishMe():
    hour = int(datetime.datetime.now().hour)                    #gets time in hours from 0 to 24
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Hyperion. Your Desktop Voice assistant. How can I help you?")


def takeCommand():                                              #takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7                                 # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"
    return query
    
def temp():                                                     #returns the temperature of the specified place
    speak("Please name the place you wish to know the temperature of.") 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.9
        audio = r.listen(source)
    try:
        print("Recognizing......")
        search = r.recognize_google(audio, language='en-in')
        print(f"User said: {search}\n")
        soup = BeautifulSoup(requests.get(f"https://www.google.com/search?q=weather+in+{search}").text,"html.parser")
        temperature = soup.find("div",class_ ="BNeawe iBp4i AP7Wnd").text
        speak(f"Current temperature of {search} is {temperature}")
        print(f"Current temperature of {search} is {temperature}")
    except Exception as e:
        #print(e)
        print("Not found")
        speak("Not found")
        print("Say that again please....")
        temp()

def gogSearch():                                                     
    speak("Please name the topic you want to search.") 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.9
        audio = r.listen(source)
    try:
        print("Recognizing......")
        search = r.recognize_google(audio, language='en-in')
        print(f"User said: {search}\n")
        url=f"https://www.google.com/search?q={search}"
        speak('Opening Google.....')
        webbrowser.get(chrome_path).open(url)
    except Exception as e:
        #print(e)
        print("Say that again please....")
        gogSearch()

def YouSearch():                                                     
    speak("Please name the video you want to search.") 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing......")
        search = r.recognize_google(audio, language='en-in')
        print(f"User said: {search}\n")
        url=f"https://www.youtube.com/results?search_query={search}"
        speak('Opening Youtube.....')
        webbrowser.get(chrome_path).open(url)
    except Exception as e:
        #print(e)
        print("Say that again please....")
        YouSearch()

def calc():
    speak("Please say the expression you want to calculate.")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing......")
        my_string=r.recognize_google(audio)
        print(my_string)
        def get_operator_fn(op):
            return{
                '+' : operator.add,
                '-' : operator.sub,
                'multiply': operator.mul,
                'multiplied by': operator.mul,
                'x': operator.mul,
                'divided':operator.__truediv__,
                'Mod' : operator.mod,
                'mod' : operator.mod,
                '^' : operator.xor,
            }[op]
        def eval_binary_expr(op1, oper, op2):
            op1,op2= int(op1), int(op2)
            return get_operator_fn(oper)(op1, op2)
        print(eval_binary_expr(*(my_string.split())))
        speak(f"The answer is {eval_binary_expr(*(my_string.split()))}")
    except Exception as e:
        #print(e)
        print("Say that again please....")
        calc()


def Find_location():          
        speak("what is the location")
        location = takeCommand().lower()
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak("Hold on , I will show you the location of " + location + " is.")

def Take_picture():
        cam = cv2.VideoCapture(0)       #o= number of devices
        cv2.namedWindow("SMILE")        #hit SPACE for SC and ESC for exit
        img_counter = 0
        while True:
            ret, frame = cam.read()     #reads your camera
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("SMILE", frame)     #shows the output to the user
            k = cv2.waitKey(1)
            if k%256 == 27:                 #hotkeys
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
        cam.release()
        cv2.destroyAllWindows()

def news():  
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "499b29c800a042a3bb0d3fdec3c57dac"                  # my generated API Key
    }
    main_url = " https://newsapi.org/v1/articles"
    res = requests.get(main_url, params=query_params)               # fetching data in json format
    open_bbc_page = res.json()
    article = open_bbc_page["articles"]                             # getting all articles in a string article
    results = []                                                    # empty list which will contain all trending news
    for ar in article:
        results.append(ar["title"])
    for i in range(len(results)):
         print(i + 1, results[i])
    speak(results)

def screenshot():
    speak("Please tell me the name for this screenshot file")
    name = takeCommand().lower()
    speak("Please hold the screen for few seconds")
    time.sleep(3)
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    speak("I am done,the screenshot is saved in our main folder")  

def time_date():
    strDate = datetime.datetime.now().strftime("%B %d %Y")
    strTime = datetime.datetime.now().strftime("%H:%M:%S") 
    speak(f"The date is {strDate} and the time is {strTime}")
    print(f"The date is {strDate} and the time is {strTime}")

def website():
    reg_ex = re.search('open website (.+)', mquery)
    if reg_ex:
        domain = reg_ex.group(1)
        print(domain)
        url = 'https://www.' + domain
        webbrowser.open(url)
        speak('The website you have requested has been opened for you.')
    else:
        pass

def status():
        usage = str(psutil.cpu_percent())
        speak("CPU is at"+usage+" percentage")
        battray = psutil.sensors_battery()
        percentage = battray.percent
        speak(f" Your system have {percentage} percentage Battery")
        if percentage >=5 and percentage <=30:
            speak("Plug to Charge")
        else:
            speak("You are good to go") 

def Internet():
        speak("Checking your internet speed!. Wait for a moment.")
        st = speedtest.Speedtest()
        down = st.download()
        down = down/(1000000) #converting bytes to megabytes
        up = st.upload()
        up = up/(1000000)
        print(down,up)
        speak(f"We have {down} megabytes per second downloading speed and {up} megabytes per second uploading speed")
        
def help():
    speak("Here are the keywords that should be in your command for following work to be done.")
    speak("Say wikipedia to search topics in Wikipedia.")
    speak("Say current date and time to know the current time and date of your system.")
    speak("Say battery to get your device battery percentage.")
    speak("Say joke to listen a joke.")
    speak("Say take screenshot to get screenshot.")
    speak("Say picture to click photos of you in webcam. Press Space bar to click and Escape key to exit.")
    speak("Say location to get location of desired place in map.")
    speak("Say open website to open that website.")
    speak("Say google search to do google search.")
    speak("Say search youtube video to search that particular video.")
    speak("Say calculate to calcute the answer of the expression.")
    speak("Say lock window to lock your device.")
    speak("Say news to get top 10 news from BBC.")
    speak("Say internet speed to get internet speed of your device.")
    speak("Say get temperature to find out tempearture of desired location.")
    speak("Say add app to add the path of your desktop applications.")
    speak("and speak help to repeat these thing again.")
        
if __name__ == "__main__":
    wishMe()
    conn=sqlite3.Connection("Database333.db")
    cur=conn.cursor()
    if os.stat("Database333.db").st_size == 0:
        speak("Please provide the apps paths to complete the setup process")
        list_of_installed_apps.start()
    while True:
        mquery = takeCommand().lower()
        cursor=conn.execute("select APPS,APPS_PATH from path")
        if mquery in mquery:
            for j in cursor:
                nquery=mquery.replace(" ","")
                nquery=nquery.replace('open','')
                vari=j[0].lower()
                vari1=vari.replace(" ","")
                if vari in 'google chrome':
                    chrome_path=j[1]+" %s"
                if vari1 in nquery:
                    speak('Opening'+nquery)
                    try:
                    #os.system('"%s"' % str(j[1]))
                        os.startfile(j[1])
                        break
                    except Exception as e:
                        print("Path not found")
                elif nquery in vari1:
                    speak('Opening '+nquery)
                    try:
                        os.startfile(j[1])
                        break
                    except Exception as e:
                        print("Path not found")
        if 'wikipedia' in mquery:                                   #returns wikipedia result
            speak('Searching Wikipedia.....')
            mquery=mquery.replace("wikipedia","")
            results=wikipedia.summary(mquery,sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'google search' in mquery:                             #searches a topic on google in google chrome
            gogSearch()
        elif 'search youtube video' in mquery:                      #searches a video on YouTube in google chrome
            YouSearch()
        elif 'open website' in mquery:
            website()
        elif 'current date and time' in mquery:                     #returns current date and time
            time_date()
        elif 'get temperature' in mquery:                           #returns current temperature of place specified
            temp()
        elif 'joke' in mquery:                                      #says joke
            speak(pyjokes.get_joke())
        elif 'calculate' in mquery:                                 #calculates expression
            calc()
        elif "take screenshot" in mquery:
            screenshot()
        elif 'add app' in mquery:
            list_of_installed_apps.start()
        elif 'list the added apps' in mquery:
            try:
                speak("Getting the list")
                conn=sqlite3.Connection("Database333.db")
                cursor=conn.execute("select APPS,APPS_PATH from path")
                cur=conn.cursor()
                for j in cursor:
                    speak(j[0])
                    print("App: ",j[0],"Path: ",j[1])
            except Exception as e:
                print("Database not found")
        elif "location" in mquery:
            Find_location() 
        elif "picture" in mquery:                   
            Take_picture()
        elif 'lock window' in mquery: 
            speak("locking the device") 
            ctypes.windll.user32.LockWorkStation()
        elif 'news' in mquery: 
            news()
        elif 'battery' in mquery:
            status()
        elif 'internet speed'in mquery:
            Internet()
        elif "how are you" in mquery:
            speak("I'm doing well, hope you are too")
        elif "who i am" in mquery or "who am i" in mquery:
            speak("If you talk then definitely you are human.")
        elif "why you came to the world" in mquery or "why do you exsist" in mquery:
            speak("Thanks to this group, further it's a secret")
        elif 'reason for you' in mquery:
            speak("I was created as a Mini project.")
        elif "who are you" in mquery:
            speak("I am Hyperion")
        elif "what do you look like" in mquery:
            speak("Imagine the feeling of a friendly hug combined with the sound of laughter. Add a librarian’s love of books, mix in a sunny disposition and a dash of unicorn sparkles, and voila!")
        elif "when is your birthday" in mquery:
            speak("We can pretend it’s today. Cake and dancing for everyone.")
        elif "help" in mquery:
            help()
        elif 'exit' in mquery or 'bye' in mquery:                                      #Exits the Hyperion
            speak('OK exiting...Thank you !')
            break
