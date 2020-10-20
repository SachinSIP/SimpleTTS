
from gtts import gTTS

import os

print("Text To Speech in 3 languages")
#Simple program to convert text to speech and save audio file in tamil and english language
while 1:
    print("")
    print("\nEnter the language first in which you want to run this 'text to speech' program\nHere are the options for you!\n")
    print("Enter '1' for tamil\n Enter '2' for British English\nEnter '3' for American English \nor Else Enter '0' to exit this program")
    print("The pronounciation may vary for tamil try different types of letter to a word and check it\n")

   
    options = ["ta","en-uk","en-us"]

    reply = int(input("Now please enter your preference : "))
    
   
    if reply<=3:
        language = options[reply-1]
    if reply==0:
        exit(0)

    mytext = input("Enter a text : ")
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("voice.mp3") 
    os.system("mpg321 voice.mp3")
