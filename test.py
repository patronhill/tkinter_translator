import speech_recognition as sr
from tkinter import *
from googletrans import Translator
from gtts import gTTS
import os
import pygame
import time

flag = 0


def tran():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        audio = r.listen(source)
        print(type(audio))

    query = r.recognize_google(audio, language='en-in')

    text = t.insert('1.0', str(query))
    a = translator.translate(query,dest='ru')
    t1.delete('1.0', END)
    t1.insert('1.0', a.text)
    speak = gTTS(text=a.text, lang='ru', slow=False)
    speak.save("captured_voice.mp3")
    time.sleep(2)
    pygame.mixer.music.load("captured_voice.mp3")
    pygame.mixer.music.play(loops=0)
    os.remove('captured_voice.mp3')
    
    
root = Tk()
root.geometry('500x350')
root.title('Переводчик')
root.resizable(width=False, height=False)
root['bg'] = 'blue'
translator = Translator()

pygame.mixer.init()

label = Label(root, fg='white', bg='black', font='Arial 15 bold', text='Say somethings')
label.place(relx=0.5, y=30, anchor=CENTER)
t = Text(root, width=35, height=5, font=('Comic Sans MS', 12, 'bold italic'))
t.place(relx=0.5, y=100, anchor=CENTER)

btn = Button(root, width=45, text='Push and Say', command=tran)
btn.place(relx=0.5, y=180, anchor=CENTER)

t1 = Text(root, width=35, height=5, font=('Comic Sans MS', 12, 'bold italic'))
t1.place(relx=0.5, y=260, anchor=CENTER)

root.mainloop()


