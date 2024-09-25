import speech_recognition as sr # type: ignore
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    pass

if  __name__ ==  "__main__":
      speak("Jarvis Load>.....")
      while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        # recognize speech using Sphinx
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "Jarvis"):
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand()
        except Exception as e:
            print("Error; {0}".format(e))