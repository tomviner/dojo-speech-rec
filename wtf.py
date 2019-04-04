#! /usr/bin/env python
import speech_recognition as sr


def rules():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak clearly")
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    # TODO: Make this do the speech recognition loop and pass off stuff to something 


rules()
