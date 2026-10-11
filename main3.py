import speech_recognition as sr
import pyttsx3
from datetime import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait()

#step 1
def get_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("????? Speak now")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"You said:{command}")
        except sr.UnknownValueError:
            print("could not understand.")
        except sr.RequestError as e:
            print(f"API Error: {e}")
    return ""

def respond_to_command(command):
    if "hello" in command :
        speak("Hi there! How can I help you today ")
    elif "your name" in command:
        speak("I am your python voice assistant")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "exit" in command or "stop" in command:
        speak("GoodBYe!")
        return False
    else:
        speak("I'm not sure how to help with that.")
    return True
def main():
    speak("Voice Assistant Activated.Say Something")
    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break
if __name__ == "__main__":
    main()