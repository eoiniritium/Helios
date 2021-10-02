import speech_recognition as sr
import PyAudio

class Helios:
    def __init__(s):
        pass

    def initiate(s):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something")
            audio = r.listen(source)

        try:
            print("Sphinx thinks you said:", r.recognize_sphinx(audio))
        except sr.UnknownValueError:
            print("Sphinx could not understand audio.")#
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))







    # Variable declarations


Helios.initiate(Helios)