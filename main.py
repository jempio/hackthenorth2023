import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
text_to_speech = pyttsx3.init()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

# Recognize the speech
try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)

    # Convert recognized text to speech
    text_to_speech.say("You said: " + text)
    text_to_speech.runAndWait()
except sr.UnknownValueError:
    print("Sorry, could not understand your speech.")
except sr.RequestError as e:
    print("Error requesting speech recognition; {0}".format(e))