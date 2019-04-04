#! /usr/bin/env python
import speech_recognition as sr
import subprocess


def act_on_will_of_people(input_text):
    respond('I understand perfectly, but this is not interesting to me.')


def respond(message):
    subprocess.check_call(['espeak', message])


def rules():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak clearly")
        audio = r.listen(source, phrase_time_limit=5)

    try:
        act_on_will_of_people(r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        respond("Sphinx could not understand audio")
    except sr.RequestError as e:
        respond("Sphinx error; {0}".format(e))


rules()
