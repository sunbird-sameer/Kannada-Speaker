##Pip installs##

# pip install gTTS


#Imports#
from gtts import gTTS
import os

while True:
    #Take input and save the speaking to a variable
    mytext = input("Enter the text in Kannada or English to speak: ")
    language = 'kn'
    myobj = gTTS(text=mytext, lang=language, slow=False)

    #Save and Play
    file_name = input("Enter the filename what you want to save the file as: ")

    myobj.save(file_name + ".mp3")
    os.system(file_name + ".mp3")
