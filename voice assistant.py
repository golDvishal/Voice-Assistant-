import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
from tkinter import *
from tkinter import filedialog
def explorer():
    def browseFiles():
        filename = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File",
                                              filetypes = (("Text files",
                                                            ".txt"),
                                                           ("all files",
                                                            ".")))
        label_file_explorer.configure(text="File Opened: "+filename)
    window = Tk()
    window.title('File Explorer')
    window.geometry("350x300")
    window.config(background = "pink")
    label_file_explorer = Label(window,
                                text = "File Explorer using Tkinter",
                                width = 50, height = 4,
                                fg = "blue")      
    button_explore = Button(window,
                            text = "Browse Files",
                            command = browseFiles) 
    button_exit = Button(window,
                         text = "Exit",
                         command = exit)
    label_file_explorer.grid(column = 1, row = 1)
    button_explore.grid(column = 1, row = 2)
    button_exit.grid(column = 1,row = 3)
    window.mainloop()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        return Query
def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',145)
    engine.say(audio)
    engine.runAndWait()
def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)
def tellTime():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak(self, "The time is sir" + hour + "Hours and" + min + "Minutes")
def Hello():
    speak("hello sir  I am  your friday . Tell me how may I help you")
def Take_query():
    while(True):
        query = takeCommand().lower()
        if "open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks ")
            webbrowser.open("www.geeksforgeeks.com")
            continue
        elif"open instagram"in query:
            speak("opening instagram")
            webbrowser.open("www.instagram.com")
        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
        elif"open youtube"in query:
                                                speak("opening youtube")
                                                webbrowser.open("www.youtube.com")
                                                continue
        elif "which day it is" in query:
            tellDay()
            continue
        elif "tell me the time" in query:
            tellTime()
            continue
        elif "bye" in query:
            speak("Bye. have a nice day")
            exit()
        elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)
        elif "tell me your name" in query:
            speak("I am friday. Your desktop Assistant")
        elif"nice name" in query:
            speak("oh thanks")
        elif"open file explorer" in query:
            explorer()
if _name_ == '_main_':
    Hello()
    Take_query()
