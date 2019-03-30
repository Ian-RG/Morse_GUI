import RPi.GPIO as GPIO
from tkinter import *
import tkinter.font
from time import sleep

dot = 0.2
dash = dot*3
componentSpace = dot
letterSpace = dot*3
wordSpace = dot*7
ledPin = 2

dict = {'a': "01", 'b': "1000", 'c': "1010", 'd': "100", 'e': "0", 'f': "0010", 'g': "110", 'h': "0000", 'i': "00", 'j': "0111", 'k': "101",'l': "0100", 'm': "11",
        'n': "10", 'o': "111", 'p': "0110", 'q': "1101", 'r': "010", 's': "000", 't': "1", 'u': "001", 'v': "0001", 'w': "011", 'x': "1001", 'y': "1011", 'z': "1100"}

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)


def flashMessage(message):
    if (len(message) > 12):
        message = message[:12]
    for i in range(len(message)):
        if (message[i].isalpha()):
            flashLetter(message[i])
            sleep(letterSpace)
        elif (message[i] == ' '):
            sleep(wordSpace)


def flashComponent(c):
    GPIO.output(ledPin, GPIO.HIGH)
    sleep(dot if c == '0' else dash)
    GPIO.output(ledPin, GPIO.LOW)


def flashLetter(letter):
    for i in range(len(dict[letter])):
        flashComponent(dict[letter][i])
        if (i < len(dict[letter])-1):
            sleep(componentSpace)


def close():
    GPIO.cleanup()
    window.destroy()


window = Tk()
window.title("Morse Code Translator")
myFont = tkinter.font.Font(family="Helvetica", size=12, weight="bold")

label = Label(text="String to translate (max 12 characters)")
label.grid(row = 0, column = 0)

e = Entry(window, font=myFont, bg="white", fg="black", width=24)
e.grid(row=1, column=0)

submitButton = Button(window, text="Submit", font=myFont, command=lambda: flashMessage(
    e.get().lower()), bg="green", height=1, width=8)
submitButton.grid(row=1, column=1)

exitButton = Button(window, text="Exit", font=myFont,
                    command=close, bg="yellow", height=1, width=12)
exitButton.grid(row=2, column=0)

window.protocol("WM_DELETE_WINDOW", close)

window.mainloop()
