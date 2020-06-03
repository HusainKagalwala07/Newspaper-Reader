def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)

if __name__ == '__main__':
    import requests
    import json
    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=e181829bb3b249c28036ec577caf063b')

    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    for i in range(0, 4):
        speak(my_json['articles'][i]['title'])