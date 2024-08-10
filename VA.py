import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Set voice (0 for male, 1 for female)
    engine.setProperty('rate', 145)  # Speed of speech
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Sorry, I didn't catch that. Could you please say that again?")
            return "None"
        return query.lower()

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    day_of_the_week = Day_dict.get(day, "Unknown")
    speak(f"Today is {day_of_the_week}")

def tellTime():
    time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {time}")

def assistant():
    speak("Hello, I am your voice assistant. How can I assist you today?")

    while True:
        query = takeCommand()

        if 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        
        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        
        elif 'what day is it' in query:
            tellDay()
        
        elif 'what time is it' in query:
            tellTime()
        
        elif 'from wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("from wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        
        elif 'exit' in query or 'bye' in query:
            speak("Goodbye, have a great day!")
            break

if __name__ == "__main__":
    assistant()
