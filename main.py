#intro
"""
    main fx where it all happens
"""
# imports
import datetime

from Text_to_Voice import speak_it
from Fx import start, wishMe, wiki, sendEmail, web_s
from speech_to_text import takeCommand
from weather import weather_report

# Global Variables
requestAI=""
requestAIs=""
i=0

# working
wishMe()
start()
while requestAIs!="exit":
    flag = 0
    
    print("SPRITAN => Sir, would you like speak or type for commanding\n\t\t press 1 to speak and 2 to type")
    speak_it("Sir, would you like to speak or type for commanding. press 1 to speak and 2 to type")
    ch = input("You     => ")
    # Checking for voice and text
    if ch == "1":
        print("SPRITAN => Plz Speak.")
        speak_it('Please Speak')
        requestAI = takeCommand()
        print("You     => "+requestAI)
    elif ch == "2":
        print("SPRITAN => Plz Command.")
        speak_it('Please command')
        requestAI = input("You     => ")

    requestAIs=requestAI.lower() #can be changed latter
    if 'wikipedia' in requestAIs:
        wiki(requestAIs)
    elif 'send email' in requestAIs:
        try:
            to = input("To: ")
            speak_it("What should I say?")
            content = input()
            sendEmail(to, content)
            speak_it("Email has been sent!")
        except Exception as e:
            print(e)
            speak_it("Sorry my friend. I am not able to send this email")
    
    elif 'web open' in requestAIs:
        web_s(requestAIs)
    
    elif requestAIs == "exit":
        print("Goodbye take care")
        speak_it("Goodbye, take care")
    
    elif 'current' in requestAIs:
        
        if 'time' in requestAIs:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak_it("Sir, the time is"+strTime)
            print("SPRITAN => Sir, the time is "+strTime)
        
        elif 'weather' in requestAIs:
            weather_report()


