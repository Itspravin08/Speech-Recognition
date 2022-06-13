# Step 1 : import pyttsx3.
import pyttsx3

# Stpe 2: initialize Text-to-speech engine.

# engine = pyttsx3.init()

convert = pyttsx3.init()

#  convert this text to speech.

# text = "Python is a great programming language"

speech = input("Enter The Sent to convert to speech : ") # Get text from User

# engine.say(text)

convert.say(speech)

# # play the speech.
# engine.runAndWait()

convert.runAndWait()