import speech_recognition as sr 
import pyttsx3
import datetime 
import pywhatkit as pk
import wikipedia as wiki
import pyjokes


engine = pyttsx3.init()
listener = sr.Recognizer()

me = "Friday"
def speak(text):
   engine.say(text)
   engine.runAndWait()

rate=engine.getProperty('rate')
engine.setProperty('rate',170)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

speak("I am your Friday. How can i assist you today?")

def take_command():
    command = ' '
    try:
       with sr.Microphone() as source:
           sr.energy_threshold = 1000 
           print("Listening...")
           voice = listener.listen(source)
           command = listener.recognize_google(voice)
           command = command.lower()
         #   if me in command:
           command = command.replace(me ," ")
            #  print(command) 
            #  speak(command)
            

          
    except:
      print("can you please say that again")
    return command

while True:
   user = take_command()
   if "time" in user:
      current_time = datetime.datetime.now().strftime('%I:%M %p')
      print("the time is  " + current_time)
      speak(current_time)
   elif "how are you" in user:
      print("i am fine sir. what about you ")
      speak("i am fine sir. what about you ")
   elif "i am good" in user:
      print("thats great to hear from you sir")
      speak("thats great to hear from you sir")
   elif "play" in user:
      song = user.replace("play"," ") 
      print("playing" + song)
      speak("playing" + song)
      pk.playonyt(song)
   elif "google" in user or "search for" in user:
      user = user.replace("google"," ")
      user = user.replace("search for"," ")
      print("searching for" + user)
      speak("searching for" + user)
      pk.search(user)
   elif "wikipedia" in user:
      user = user.replace("wikipedia"," ")
      info = wiki.summary(user,2)
      print(info)
      speak(info)
   elif "joke" in user:
      joke = pyjokes.get_joke()
      print(joke)
      speak(joke) 
   elif "exit" in user:
      print("see you again. Goodbye ")
      speak("see you again. Goodbye ")
      exit()



