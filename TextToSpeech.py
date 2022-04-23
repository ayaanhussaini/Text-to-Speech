import playsound   # library to play sound
from tkinter import *   # gui library
from gtts import gTTS   # text to speech library

# function to convert text to speech
def speak():
    textInput = textBox.get()  # getting text to translate
    tts = gTTS(text=textInput, lang='en')   # initiating gtts
    filename = "speech.mp3"  # can change name of file
    tts.save(filename)   # saving file
    playsound.playsound(filename) # playing sound
    # textBox.delete(0, END)  # remove comment to delete text field after playing audio


# making the gui
root = Tk()
root.title('Text to Speech')
root.geometry('500x300')

# creating text field
text = StringVar()
info = Label(text= 'Enter text below:')
textBox = Entry(textvariable = text, width = 40)
textBox = Entry(bd=1, highlightcolor= 'SteelBlue3')
info.pack(pady=20)
textBox.pack(pady=30)

# creating button
buttonToSpeak = Button( text='Speak', command=speak)
buttonToSpeak.pack(pady=20)

root.mainloop()


