"""
Use News API websites for current affairs.
Then make program to speak the newses one by one.
"""

from win32com.client import Dispatch
import requests
import json
import pyttsx3


def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)


if __name__ == '__main__':
    speak("News for Today.. Lets begin")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=09def55c3971413f8b7882b3f8f56979"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict["articles"]

    i = 1
    for article in arts:
        print(f"news{i} --> {article['title']} --> {article['publishedAt']}")
        speak(article['title'])
        i += 1
        if i < len(arts) + 1:
            speak(f"Moving on to News number {i}.. Listen Carefully")
        else:
            speak("Thanks for listening")
            speak("If you also want to make such type of program then contact to saksham")
