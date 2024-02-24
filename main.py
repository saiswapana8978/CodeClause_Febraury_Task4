import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki
import webbrowser
from tkinter import *
from PIL import ImageTk, Image

listener = sr.Recognizer()
speaker = pyttsx3.init()
speaker.setProperty('rate', 150)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)

def speak(text):
    speaker.say(text)
    speaker.runAndWait()
va_name = 'lesa'

def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1)
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if va_name in command:
                command = command.replace(va_name+' ', '')

    except:
        print("Check Your Microphone")
    return command

class Widget:
    def __init__(self):

        root = Tk()
        root.title('lesa')
        root.geometry('520x320')
        root.resizable(FALSE, FALSE)

        userText = StringVar()
        userText.set('Your Virtual Assistant')

        userFrame = LabelFrame(root, text='Lesa', font=('Railways', 24, 'bold'))
        userFrame.pack(side='left', fill='both', expand=1)
        text = Message(userFrame, textvariable=userText, bg='black', fg='white')
        text.config(font=("Century Graphic", 15, 'bold'))
        text.pack(side='top', fill='both', expand=1)

        btn = Button(root, text='Run', font=('railways', 10, 'bold'), bg='red', fg='white',command=self.clicked).pack(fill='x', expand=0)
        btn2 = Button(root, text='Close', font=('railways', 10, 'bold'), bg='yellow', fg='black',
                      command=root.destroy).pack(fill='x', expand=0)

        img = ImageTk.PhotoImage(Image.open('lesa_img.jpg'))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand=0)

        root.mainloop()
    def clicked(self):
        speak('Hello! I am your ' + va_name + ', How can I help you??')
        while True:
            user_command = take_command()
            if 'exit' in user_command:
                print('See you again, Great talking to you!!')
                speak('See you again, Great talking to you!!')
                break
            elif 'time' in user_command:
                cur_time = dt.datetime.now().strftime("%I:%M %p")
                print(cur_time)
                speak("It's " + cur_time + " Now ")
            elif 'play' in user_command:
                user_command = user_command.replace('play ', '')
                print('playing ' + user_command)
                speak('playing ' + user_command)
                pk.playonyt(user_command)
                break
            elif 'search' in user_command:
                user_command = user_command.replace('search ', '')
                print('Searching for ' + user_command)
                speak('Searching for ' + user_command)
                pk.search(user_command)
            elif 'what is' in user_command or 'who is' in user_command:
                user_command = user_command.replace('who is ','')
                user_command = user_command.replace('what is ', '')
                info = wiki.summary(user_command, 4)
                print(info)
                speak(info)
            elif 'who are you' in user_command:
                speak('Iam your ' + va_name + ', Tell me what you want')
            elif 'location' in user_command:
                user_command = user_command.replace('location of ', '')
                url = "https://google.nl/maps/place/" + user_command + '/&amp;'
                webbrowser.get().open(url)
                speak('Here is the location' + user_command)
            else:
                speak('Please say it again')

if __name__=='__main__':
    w = Widget()
