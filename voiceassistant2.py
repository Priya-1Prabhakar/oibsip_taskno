import speech_recognition as sr
import datetime
import random
import pyttsx3
import webbrowser

# Greeting responses
greetings = ["Hello!", "Hi there!", "Hey, how can I help you?", "Hi! What can I do for you today?"]

# Initialize the recognizer and speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Main loop
while True:
    # Listen for user input
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        # Use of Google recognition speech recognition
        command = r.recognize_google(audio)

        # Process user commands
        if "hello" in command:
            response = random.choice(greetings)
            print(command)
        elif "time" in command:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M")
            print(command)
            print("The current time is ",current_time)
            response = f"The current time is {current_time}."
        elif "date" in command:
            now = datetime.datetime.now()
            current_date = now.strftime("%B %d, %Y")
            print(command)
            print("Today's date is" ,{current_date})
            response = f"Today's date is {current_date}."
        elif "search" in command:
            query = command.replace("search", "")
            webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
            response = f"Here are the search results for '{query}'"
            print(command)
        elif "bye" in command:
            print(command)
            response = f"bye! see you again..."
            break
        else:
            response = "I'm sorry, I didn't understand that command."

    except sr.UnknownValueError:
        response = "Sorry, I couldn't understand your command."
    except sr.RequestError:
        response = "Sorry, there was an issue with the speech recognition service."

    # Speak the response
    engine.say(response)
    engine.runAndWait()
