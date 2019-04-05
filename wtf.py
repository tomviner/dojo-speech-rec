#! /usr/bin/env python
import subprocess
import webbrowser
from urllib.parse import quote_plus

import speech_recognition as sr

from search import get_image_url


def act_on_will_of_people(input_text):
    respond(input_text)
    respond('I understand perfectly, but this is not interesting to me.')


def say_will_of_people(text):
    respond(f'Did you mean: {text}?')
    hear()
    respond(f'{text} means {text}! And weve made a success of it')


    url = get_image_url(text)
    webbrowser.open_new(url)


def respond(message):
    subprocess.check_call(['say', message])


def hear():
    r = sr.Recognizer()
    print("Speak clearly")
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=2)
    return r.recognize_sphinx(audio)


def main():
    try:
        text = hear()
        say_will_of_people(text)
        # act_on_will_of_people(r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        respond("Sphinx could not understand audio")
    except sr.RequestError as e:
        respond("Sphinx error; {0}".format(e))


main()
