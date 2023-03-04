import audioop
import wikipedia
import pyttsx3
import datetime
import webbrowser
import os
import speech_recognition as sr
from playsound import playsound
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

# Takes user's commands and prints it in console(Text to speech)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"{name}:{query} \n")

    except Exception as e:
        print(e)
        print("Say that again please..")

        return "none"
    return query
# Redirects to chrome instead of edge
def search(url):
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe "
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(url)

# Voice of AI
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
name='Sahil'
# Greeting funtion
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning {name}")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon {name}")
    else:
        speak(f"Good Evening {name}")

    speak("I am kronos....how may i help you?")

if __name__ == "__main__":
    wishMe()
    while(True):
        query = takeCommand().lower()

         # Searches on web
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            print("According to wikipedia....")
            print(results)
            speak("According to wikipedia....")
            speak(results)

        elif 'open youtube' in query:
            speak('Opening youtube')
            url='youtube.com'
            search(url)
            
        elif 'open facebook' in query:
            speak('Opening facebook')
            url="www.facebook.com"
            search(url)
                
                    
        elif 'open google' in query:
            speak('Opening google')
            url='google.com'
            search(url)
        elif 'open instagram' in query:
            speak('Opening instagram')
            url='instagram.com'
            search(url)

        elif 'open whatsapp' in query:
            speak('Opening whatsapp')
            url='web.whatsapp.com'
            search(url)

        elif 'the time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        elif 'open chrome' in query:
            speak('Opening chrome')
            chromePath= "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif 'open discord' in query:
            speak('Opening discord')
            os.system(r'C:\\Users\husai\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe')
                

        elif 'open notepad' in query:
            speak('Opening notepad')
            os.system(r'%windir%\\system32\\notepad.exe')

        #searching on google
        elif 'google' in query:
            queryspeak=query.replace("search google for","")
            query=query.replace("search google for","")
            speak(f'searching google for {queryspeak}')
            search(f'https://www.google.com/search?q={query}')

        # Searching on youtube
        elif 'search youtube' in query:
            queryspeak=query.replace("search youtube for","")
            query=query.replace("search youtube for ","")
            speak(f'searching youtube for {queryspeak}')
            search(f'https://www.youtube.com/results?search_query={query}')

        
        # Searching on amazon
        elif 'amazon' in query:
            query=query.replace("search amazon for"," ")
            speak(f'here is what i found')
            search(f'https://www.amazon.in/s?k={query}')

        # Exists the assistant
        elif 'exit' in query:
            speak("Glad i can be of help...shutting down")
            break 
        # Sending Whatsapp messages:
        elif 'send whatsapp text' in query:
            users={"Uzma": "+916392973570","test":"+919305975675","aman":"+917987906507" , "appi" :"+917985641557"}
            speak("What is your message?")
            message=takeCommand()
            speak('Who do you want to send this message to?')
            try:
                recipientname=takeCommand().lower()
                recipientnum=users[recipientname]
                pywhatkit.sendwhatmsg_instantly(recipientnum,message,5)
            except Exception as e:
                print(e)
                print("Try again please")
        # turns off computer
        elif "turn off my system" in query:
            pywhatkit.shutdown(time=2)

        elif "play" in query:
            query=query.replace("play"," ")
            query=query.replace("search"," ")
            speak(f'playing {query}')
            pywhatkit.playonyt(query)