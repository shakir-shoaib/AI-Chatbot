import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests 
import openai
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "5c9e46a61cd44f8594e567fa2900d44a"

def speak(text):
    engine.say(text)
    engine.runAndWait()
def aiProcess(command):
    system_content = "You are a virtual assistant"
    user_content = command
    client = openai.OpenAI(
    api_key="97284029bed54de8bc71f362a23b6938",
    base_url="https://api.aimlapi.com",
    )
    chat_completion = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    messages=[
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ],
    temperature=0.7,
    max_tokens=128,
    )

    response = chat_completion.choices[0].message.content
    return response
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin f.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={newsapi}")                   
        if r.status_code == 200:
    # Parse the JSON response
            data = r.json()
    
    # Extract and print headlines
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
    else:
        output = aiProcess(c)
        speak(output)       
if __name__  == "__main__":
    speak("Initializing Jarvis.....")
    while True:
    # Listen for the wake word "Jarvis"
    # obtain audio from the microphone
        r = sr.Recognizer()
        

        try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source, timeout=3, phrase_time_limit=1)
                    command = r.recognize_google(audio)

                    processCommand(command)  
        except Exception as e:
            print("Error; {0}".format(e))  