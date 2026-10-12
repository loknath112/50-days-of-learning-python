#problem 2
#use the elxternal module also install one 
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("hello everyone i am  ashok and i am learning python programming language")
engine.runAndWait()