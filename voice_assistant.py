import speech_recognition as sr #convert speech to text
import datetime #for fetching date and time
import wikipedia
import webbrowser
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os # to save/open files
import wolframalpha # to calculate strings into formula
import time
import pyjokes

def talk():
    input = sr.Recognizer()
    with sr.Microphone() as source:
        audio = input.listen(source)
        data = ""
        try:
            data = input.recognize_google(audio)
            print("Your question is, " + data)

        except sr.UnknownValueError:
            print("Sorry I did not hear your question, Please repeat again.")


    return data

def respond(output):
    num=0
    print(output)
    num += 1
    response=gTTS(text=output, lang='en')
    file = str(num)+".mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)


if __name__ == '__main__':
    respond("Hi, Myself Sunday here to help you ")

    while (1):
        respond("How can I help you?")
        text = talk().lower()

        if text == 0:
            continue

        if "stop" in str(text) or "exit" in str(text) or "bye" in str(text):
            respond("Ok bye and take care")
            break

        if 'wikipedia' in text:
            respond('Searching Wikipedia')
            dru = text.replace("wikipedia", "")
            dru = ''.join(c for c in dru if c.isalpha())
            results = wikipedia.summary(dru, sentences=3)
            respond("According to Wikipedia")
            respond(results)

        if 'time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"the time is {strTime}")

        if 'search' in text:
            dru = text.replace("search", "")
            try:
                from googlesearch import search
            except ImportError:
                print("No module named 'google' found")

            respond("Below are the list of websites available")

            for j in search(dru, tld="co.in", num=10, stop=10, pause=2):
                print(j)

        if "calculate" in text:
            app_id = "6Y8GPL-JR98X35TTJ"
            client = wolframalpha.Client(app_id)
            query = text.split()[1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            respond("The answer is " + answer)

        if 'joke' in text:
            respond(pyjokes.get_joke())

        if "who am i" in text:
            respond("I am guessing you are my creator, Arpan")

        if 'open google' in text:
            webbrowser.open_new_tab("https://www.google.com")
            respond("Google is open")
            time.sleep(5)

        if 'spotify' in text:
            respond("Spotify is open")
            os.system("Spotify")

        if "youtube" in text:
            respond("Opening youtube")
            webbrowser.open_new("youtube.com")

        if text != "":
            c=0
            for i in ("time", "youtube", "wikipedia", "who am i", "spotify", "google", "joke", "calculate", "search"):
                if i not in text:
                    c=c+1
            if(c==9):
                respond("Application not available")
