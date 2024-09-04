import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("goodmorning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("HI i am Lansy please telme how can i help you")



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
        r.pause_threshold = 1

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=7)  # Increase timeout and add phrase_time_limit
        except sr.WaitTimeoutError:
            print("Could not request results from Google Speech Recognition service; no speech detected.")
            return 'None'

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return 'None'
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return 'None'
    
    return query

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('tempy418@gmail.com','Nanhattan@63')
    server.sendmail('sinhasanket160@gmail.com',to,content)
    server.close()
    


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir = 'C:\\Users\\DELL\\OneDrive\\Desktop\\New Desktop\\Jarvis\\music'  # Specify the directory where your music files are stored
            songs = os.listdir(music_dir)
            print(songs)  # Prints the list of songs
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "send email to nexia" in query:
            try:
                speak("what should i say")
                content = takecommand()
                to="nexia2107@gmail.com"
                sendemail(to,content)
                speak("Email gas beeen sent!")
            except Exception as e:
                print(e)
                speak("Sorry i am not able to send this email at the moment")


