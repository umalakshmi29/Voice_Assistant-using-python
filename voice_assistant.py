import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes
from PIL import ImageGrab
import os



'''
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0])
engine.setProperty('voice',voices[0].id)
'''
def speak(audio):
    try:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()
        engine.stop()   # make sure engine is closed after speaking
    except Exception as e:
        print(f"TTS Error: {e}")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

speak("I am Jarvis Sir. Please tell me how may I help you")
        
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

  

if __name__ == "__main__":
    wishMe()
    while True:
        #query = takeCommand().lower()
        query = takeCommand()
        if query == "None":
            continue
        query = query.lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
            
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        elif 'open spotify' in query:
            speak("Opening spotify")
            webbrowser.open("spotify.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'date' in query:
           today = datetime.datetime.now().strftime("%A, %d %B %Y")
           speak(f"Today's date is {today}")

        elif 'open word' in query:
            speak("Opening M S Word")
            codePath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)
        elif 'joke' in query:
           joke = pyjokes.get_joke()
           speak(joke)
           print(joke)
        elif 'remember' in query:
           speak("What should I remember?")
           data = takeCommand()
           with open("notes.txt", "a") as f:
             f.write(data + "\n")
           speak("I will remember that")
        elif 'do you remember' in query:
           with open("notes.txt", "r") as f:
             notes = f.read()
           speak("You asked me to remember this")
           speak(notes)
   
        elif 'screenshot' in query:
            screenshot = ImageGrab.grab()
            screenshot.save("screenshot.png")
            speak("Screenshot has been taken and saved as screenshot.png")

        elif 'quit' in query or 'exit' in query or 'stop' in query:
            speak("Goodbye Sir, have a great day!")
            break

    
