import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import time
import random

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech and print
def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# Function to listen for user commands
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        speak("Sorry, I didn't understand.")
        return None
    except sr.RequestError as e:
        print("Sorry, there was an error. Check your internet connection.")
        speak("Sorry, there was an error. Check your setup.")
        speak(str(e))
        return None

# Function to get the current time
def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    return current_time

# Function to get the current date
def get_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%B %d, %Y")
    return current_date

# Function to get details about the AI
def get_details():
    details = "I am an AI assistant programmed to tell time, provide the date, tell jokes, sing songs, and perform web searches."
    return details

# Function to sing a song with auto-tune effect
def sing_song():
    song_lyrics = """
    Twinkle, twinkle, little star,
    How I wonder what you are!
    Up above the world so high,
    Like a diamond in the sky.
    Twinkle, twinkle, little star,
    How I wonder what you are!
    """
    lines = song_lyrics.splitlines()
    for line in lines:
        speak(line)
        time.sleep(0.5)  # Adjust the delay for better rhythm

# Function to tell a joke
def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you get when you cross a snowman and a vampire? Frostbite."
    ]
    joke = random.choice(jokes)
    speak(joke)

# Function to search the web
def search_web(query):
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)
    speak(f"Searching the web for {query}")

# Main program loop
while True:
    speak("How can I assist you?")
    command = listen()

    if command:
        if "exit" in command or "quit" in command:
            speak("Goodbye!")
            break

        if "hello" in command:
            speak("Hello! How can I assist you today?")

        elif "time" in command:
            current_time = get_time()
            speak("The current time is " + current_time)

        elif "date" in command:
            current_date = get_date()
            speak("Today's date is " + current_date)

        elif "details" in command or "about you" in command:
            assistant_details = get_details()
            speak(assistant_details)

        elif "joke" in command or "tell me a joke" in command:
            tell_joke()

        elif "sing" in command or "sing a song" in command:
            speak("Sure! Here's a song for you.")
            sing_song()
        elif "good morning" in command:
            speak("Good morning! How are you today?")

        elif "good night" in command:
            speak("Good night! Sweet dreams.")

        elif "good evening" in command:
            speak("Good evening! How was your day?")

        elif "good afternoon" in command:
            speak("Good afternoon! I hope you're having a good day.")

        elif "thank you" in command:
            speak("You're welcome!")

        else:
            search_web(command)
        
        # Add a slight delay before asking again
        time.sleep(1)
