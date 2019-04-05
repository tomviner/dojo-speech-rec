import speech_recognition as sr
import webbrowser
from urllib.parse import quote_plus


def hear():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak clearly")
        audio = r.listen(source, phrase_time_limit=2)
        print('.')

    return r.recognize_sphinx(audio)


def url_opener(text):
    webbrowser.open_new(
        f"https://www.google.com/search?q={quote_plus(text)}&tbm=isch"
    )


if __name__ == "__main__":
    text = hear()
    print(text)
    url_opener(text)
