#intro
"""
    this module is for all random feature and functions which are not too big to have separate modules
"""
#import
import datetime
import wikipedia
import smtplib
import webbrowser

from Text_to_Voice import speak_it

# Start welcome function
def start ():
    print("=> Hello, This is SPRITAN a chatbot AI")
    speak_it("Hello, This is SPRITAN a chatbot AI")
    print("=> Feel free to say hi or command me to do something")
    speak_it("Feel free to say hi or command me to do something")
    print("-------------------------------------------------------------------------------------")

#wish me
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak_it("Good Morning!")
    elif hour>=12 and hour<18:
        speak_it("Good Afternoon!")   
    else:
        speak_it("Good Evening!")  

#wikipedia
 # Logic for executing tasks based on query
def wiki(query):
    speak_it('Searching Wikipedia...')
    print("Searching Wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak_it("According to Wikipedia")
    print("SPRITAN => According to Wikipedia")
    print(results)
    speak_it(results)
    
# email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

# Web
def web_s(query):
    if 'youtube' in query:
        speak_it('Opeaning Youtube')
        print("SPRITAN => Opeaning Youtube")
        webbrowser.open("https://www.youtube.com/", new=2)
    elif 'google' in query:
        webbrowser.open("https://www.google.com/", new=2)
    elif 'stackoverflow' in query:
        webbrowser.open("https://stackoverflow.com",new=2)
    
