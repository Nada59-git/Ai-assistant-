import datetime
import speak
import webbrowser
import weather
import os


def Action(send):  
    data_btn = send.lower()

    if "what is your name" in data_btn:
        speak.speak("My name is Echo")  
        return "My name is Echo"

    elif "hello" in data_btn: 
        speak.speak("Hey sir, How can I help you?")  
        return "Hey sir, How can I help you?" 

    elif "how are you" in data_btn:
        speak.speak("I am doing great, thank you!") 
        return "I am doing great, thank you!"   

    elif "thank you" in data_btn:
        speak.speak("It's my pleasure to assist you!")
        return "It's my pleasure to assist you!"      

    elif "good morning" in data_btn:
        speak.speak("Good morning! How can I assist you?")
        return "Good morning! How can I assist you?"   

    elif "time now" in data_btn:
        current_time = datetime.datetime.now()
        Time = f"{current_time.hour} Hour : {current_time.minute} Minute" 
        speak.speak(Time)
        return Time

    elif "shutdown" in data_btn or "quit" in data_btn:
        speak.speak("Okay sir, shutting down.")
        return "ok sir"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")   
        speak.speak("gaana.com is now ready for you, enjoy your music!")                   
        return "gaana.com is now ready for you, enjoy your music!"

    elif "open google" in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("Google is open.")  
        return "Google is open."

    elif "youtube" in data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube is open.") 
        return "YouTube is open."    
    
    elif 'weather in' in data_btn:
        # Extract city name after "weather" keyword
        city = data_btn.replace("weather in", "").strip()
        if not city:
            return "Please specify a city for the weather forecast."
        ans = weather.Weather(city)
        return ans
        
    else:
        speak.speak("I'm not able to understand!")
        return "I'm not able to understand!"



